"""Plain-text extraction for local source uploads; no OCR or document execution."""
from io import BytesIO
from pathlib import Path
import zipfile
from xml.etree import ElementTree

MAX_BYTES = 10 * 1024 * 1024
MAX_CHARS = 500_000


def pdf_to_markdown(filename: str, pages: list[str]) -> str:
    """Wrap extracted page text without claiming inferred document structure."""
    # Escape the display name as plain Markdown text, not HTML or an instruction.
    name = Path(filename).name.replace('\n', ' ').replace('\r', ' ')
    for character in ('\\', '`', '*', '_', '[', ']', '<', '>', '#'):
        name = name.replace(character, '\\' + character)
    notice = ('Text extraction only. Page headings are generated locators; document layout, '
              'tables, images, and heading hierarchy have not been reconstructed. '
              'Check the original PDF for reading order and missing visual content.')
    return f'# Source: {name}\n\n> {notice}\n\n' + '\n\n'.join(
        f'## Page {index}\n\n{text.strip()}' for index, text in enumerate(pages, 1)
    )


def extract_source(filename: str, data: bytes) -> str:
    if not data or len(data) > MAX_BYTES:
        raise ValueError("Upload a nonempty file no larger than 10 MB.")
    suffix = Path(filename).suffix.lower()
    try:
        if suffix in {".txt", ".md"}:
            text = data.decode("utf-8-sig")
        elif suffix == ".pdf":
            from pypdf import PdfReader
            reader = PdfReader(BytesIO(data))
            if reader.is_encrypted:
                raise ValueError("Password-protected PDFs are not supported. Upload an unlocked copy.")
            if len(reader.pages) > 200:
                raise ValueError("PDFs are limited to 200 pages. Split the source into smaller files.")
            pages = []
            for i, page in enumerate(reader.pages, 1):
                value = page.extract_text() or ""
                if not value.strip():
                    raise ValueError(f"PDF page {i} has no extractable text. OCR is not supported; provide a text version.")
                pages.append(value)
                if sum(map(len, pages)) > MAX_CHARS:
                    raise ValueError("Extracted text exceeds 500,000 characters. Split the source.")
            text = pdf_to_markdown(filename, pages)
        elif suffix == ".docx":
            with zipfile.ZipFile(BytesIO(data)) as archive:
                info = archive.getinfo("word/document.xml")
                if info.file_size > MAX_BYTES:
                    raise ValueError("The DOCX text content is too large. Split the source.")
                root = ElementTree.fromstring(archive.read(info))
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            paragraphs = []
            for paragraph in root.findall(".//w:p", ns):
                parts = []
                for node in paragraph.iter():
                    tag = node.tag.rsplit("}", 1)[-1]
                    if tag == "t": parts.append(node.text or "")
                    elif tag == "tab": parts.append("\t")
                    elif tag in {"br", "cr"}: parts.append("\n")
                paragraphs.append("".join(parts))
            text = "\n".join(paragraphs)
        else:
            raise ValueError("Supported formats: TXT, Markdown, PDF, and DOCX.")
    except UnicodeDecodeError as exc:
        raise ValueError("Save the text file with UTF-8 encoding and try again.") from exc
    except ValueError:
        raise
    except Exception as exc:
        raise ValueError("The file could not be read. Check its format or provide a text copy.") from exc
    text = text.strip()
    if not text or "\x00" in text:
        raise ValueError("No usable text was found. Provide a text version of the source.")
    if len(text) > MAX_CHARS:
        raise ValueError("Extracted text exceeds 500,000 characters. Split the source.")
    return text
