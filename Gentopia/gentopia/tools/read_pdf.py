from typing import AnyStr
from PyPDF2 import PdfReader
from gentopia.tools.basetool import *


class ReadPdfArgs(BaseModel):
    file_path: str = Field(..., description="Path to the PDF file to read")


class ReadPdf(BaseTool):
    """Tool that reads text from a PDF file."""

    name = "read_pdf"
    description = "Tool that reads text from a PDF file."

    args_schema: Optional[Type[BaseModel]] = ReadPdfArgs

    def _run(self, file_path: AnyStr) -> str:
        text = ""
        with open(file_path, "rb") as file:
            pdf_reader = PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        return text

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    ans = ReadPdf()._run("example.pdf")
    print(ans)

