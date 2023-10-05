import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_ocr.json'
# pip install google-cloud-documentai
from google.cloud import documentai
from google.api_core.client_options import ClientOptions

endpoint = 'documentai.googleapis.com'
location = 'us' # Format is 'us' or 'eu'
project_id = 'AQUI PEGA EL ID DE TU PROYECTO DE GOOGLE CLOUD PLATAFORM'
processor_id = 'AQUI PEGA EL ID DE TU PROCESADOR DE OCR DEL SERVICIO DE DOCUMENT AI' # Create processor in Cloud Console


def get_text_from_pdf_ocr(file_path):
    try:
        mime_type = 'application/pdf'
        client = documentai.DocumentProcessorServiceClient(
            client_options=ClientOptions(api_endpoint=f"{location}-{endpoint}"))
        name = client.processor_path(project_id, location, processor_id)
        with open(file_path, "rb") as image:
            image_content = image.read()
        
        raw_document = documentai.RawDocument(
            content=image_content, mime_type=mime_type)
        
        request = documentai.ProcessRequest(name=name, raw_document=raw_document)
        response = client.process_document(request=request)
        document = response.document
        return document.text
    except Exception as e:
        print(e)
        return None
    
if __name__ == '__main__':
    file_path = 'muni_ocr.pdf'
    text = get_text_from_pdf_ocr(file_path)
    
    with open('muni_ocr.txt', 'w', encoding='utf-8') as f:
        f.write(text)