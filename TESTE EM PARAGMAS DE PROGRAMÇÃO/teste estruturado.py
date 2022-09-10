# %%
#! pip install FPDF

# %%
from fpdf import FPDF
from PIL import Image

# %%
listaImagens = []
listaPages=[]
for i in range(1,147):
    #i.toString()
# Abra a imagem | Coloque o local da imagem!
     im1 = Image.open(r'C:\Users\dougl\Desktop\projetos\python\fotos-20210624T144130Z-001\sapato\sapatos ('+str(i)+').jpg')
     listaImagens.append(im1)
     caminho = r'C:\Users\dougl\Desktop\projetos\python\fotos-20210624T144130Z-001\sapato\sapatos ('+str(i)+').jpg'
     listaPages.append(caminho)

pdfFileName = 'catalogo de sapatos'
dir = ''
if (dir):
    dir += "/"

cover = listaImagens[0]
width, height = cover.size

pdf = FPDF(unit = "pt", format = [width, height])
    

for page in listaPages:
    pdf.add_page()
    pdf.image(page, 0, 0)

pdf.output(dir + pdfFileName + ".pdf", "F")


