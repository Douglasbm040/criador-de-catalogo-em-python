
#! atenção obrigatorio instalar esta biblioteca
# ! pip install FPDF
#

from fpdf import FPDF
from PIL import Image


local_das_imagens='C:\\Users\\dougl\\Desktop\\projetos\python\\fotos-20210624T144130Z-001\\sapato\\'


class Imagem : 
     
    def localizar_imagens (nome_da_imagem,local_das_imagens, numero_de_imagens):
        listaImagens = []
        listaPages= [] 
        for i in range(1,numero_de_imagens + 1):
             imagem = Image.open(local_das_imagens + nome_da_imagem+' (' + str(i) + ').jpg')
             listaImagens.append(imagem)
             caminho = local_das_imagens + nome_da_imagem +' ('+str(i) + ').jpg'
             listaPages.append(caminho)
        return imagem , caminho 

class Pdf:
    def fabricar_PDF (batizar_pdf,imagem,caminho):
        pdfFileName = batizar_pdf
        dir = ''
        
        if (dir):
            dir += "/"
        
        cover = imagem
        width, height = cover.size
        pdf = FPDF(unit = "pt", format = [width, height])
        
        for page in caminho:
            pdf.add_page()
            pdf.image(page, 0, 0)
        
        return pdf.output(dir + pdfFileName + ".pdf", "F")

imagem=Imagem.localizar_imagens('sapatos',local_das_imagens , 147)
Pdf.fabricar_PDF('CATALOGO', imagem[0], imagem[1])
#Imagem = Imagem()
