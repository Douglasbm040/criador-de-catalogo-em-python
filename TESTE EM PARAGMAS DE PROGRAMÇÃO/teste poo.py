# %%
# Importe a biblioteca
from PIL import Image

listaImagens = []
for i in range(1,395):
    #i.toString()
# Abra a imagem | Coloque o local da imagem!
     im1 = Image.open(r"C:\Users\dougl\Desktop\projetos\python\fotos-20210624T144130Z-001\fotos\imagens ("+str(i)+').jpg')
     listaImagens.append(im1)
 # Defina uma lista com as imagens

for i in listaImagens:
#  # Coloque a imagem dentro de um PDF chamado arquivo.pdf
    i.save("catalogo.pdf", "PDF" ,resolution = 100.0, save_all=True, append_image=listaImagens)

# %%
#! pip install FPDF


# %%


# %%

def makePdf(pdfFileName, listPages, dir = ''):
    if (dir):
        dir += "/"

    cover = Image.open(dir + str(listPages[0]) + ".jpg")
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])
    

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page) + ".jpg", 0, 0)

    pdf.output(dir + pdfFileName + ".pdf", "F")

# %%
def criarpdf(pdfFileName,listapages,dir = ''):

    if (dir):
        dir += "/"

    cover = Image.open(listaPages[0])
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])
    

    for page in listaPages:
        pdf.add_page()
        pdf.image(page, 0, 0)

    pdf.output(dir + pdfFileName + ".pdf", "F")

# %%
sapatos=r'C:\Users\dougl\Desktop\projetos\python\fotos-20210624T144130Z-001\sapato'
bolsas=r'C:\Users\dougl\Desktop\projetos\python\fotos-20210624T144130Z-001\bolsas'
lista_de_caminhos(147,sapatos)
criarpdf('oi',lista_de_caminhos)

# %%
from fpdf import FPDF
from PIL import Image
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

# %%
from fpdf import FPDF
from PIL import Image
# deve renomear as imagens com mesmo nome 
# selecione tudo usando 'crtl + a', selecione renomear e digite um nome para padronizar todos os arquivos
# exemplo para declarar o caminho do arquivos \\
imagem='C:\\Users\\dougl\\Desktop\\projetos\python\\fotos-20210624T144130Z-001\\sapato\\'

# %%
def imagens (nome_da_imagem,local_das_imagens,numero_de_imagens):
    listaImagens = []
    listaPages=[]
    for i in range(1,numero_de_imagens+1):
        #i.toString()
    # Abra a imagem | Coloque o local da imagem!
         imagem = Image.open(local_das_imagens+nome_da_imagem+str(i)+').jpg')
         listaImagens.append(imagem)
         caminho =local_das_imagens+nome_da_imagem
        +str(i)+').jpg'
         listaPages.append(caminho)
    return imagem , caminho 

# %%
def fabricar_PDF (batizar_pdf,imagem,caminho):
    pdfFileName = 'catalogo de sapatos'
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

# %%
imagens('sapatos ',imagem,146)

# %%


# %%



