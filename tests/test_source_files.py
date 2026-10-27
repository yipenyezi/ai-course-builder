from io import BytesIO
import unittest
import zipfile

from src.source_files import extract_source, pdf_to_markdown


class SourceTests(unittest.TestCase):
    def test_markdown_preserves_page_text_and_order(self):
        markdown = pdf_to_markdown('sample.pdf', ['First page: 25%.', 'Second page: exception applies.'])
        self.assertIn('## Page 1\n\nFirst page: 25%.', markdown)
        self.assertIn('## Page 2\n\nSecond page: exception applies.', markdown)
        self.assertLess(markdown.index('First page'), markdown.index('Second page'))
        self.assertIn('have not been reconstructed', markdown)

    def test_text_and_invalid_inputs(self):
        self.assertEqual(extract_source('notes.MD', b'\xef\xbb\xbfSynthetic source'), 'Synthetic source')
        for name, data in [('empty.txt', b''), ('image.png', b'fake'), ('bad.txt', b'\xff'), ('bad.pdf', b'not a PDF')]:
            with self.assertRaises(ValueError):
                extract_source(name, data)

    def test_docx_paragraph_table_and_tabs(self):
        data = BytesIO()
        with zipfile.ZipFile(data, 'w') as archive:
            archive.writestr('word/document.xml', '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>First</w:t><w:tab/><w:t>part</w:t></w:r></w:p><w:tbl><w:tr><w:tc><w:p><w:r><w:t>Cell</w:t></w:r></w:p></w:tc></w:tr></w:tbl></w:body></w:document>')
        self.assertEqual(extract_source('source.docx', data.getvalue()), 'First\tpart\nCell')

    def test_blank_pdf_is_not_silently_accepted(self):
        from pypdf import PdfWriter
        writer = PdfWriter()
        writer.add_blank_page(width=100, height=100)
        buffer = BytesIO()
        writer.write(buffer)
        with self.assertRaisesRegex(ValueError, 'OCR'):
            extract_source('scan.pdf', buffer.getvalue())
