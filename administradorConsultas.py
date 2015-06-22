from descarga import Descarga
import xml.etree.ElementTree as ET
import os
REPOSITORY_DIR=REPOSITORY_DIR = "/home/vigtech/shared/repository/"
class AdministradorConsultas:
    titulos_descargas = []
    eids_descargas = []
    lista_docs=[]
    def __init__(self):
        self.consultas = []
        self.lista_docs=[]
        UNIVERSIDAD_sin_cerrar_parantesis = ' ( AFFIL ( universidad  AND  del  AND  valle )  OR  AF-ID ( 60066812 ) ) '
        UNIVERSIDAD = ' ( AFFIL ( universidad  AND  del  AND  valle )  OR  AF-ID ( "Universidad del Valle"  60066812 ) ) )'
        #self.consultas.append('( AFFIL ( ing*  AND  sist*  AND  comp* )  OR  AFFIL ( eng*  AND  sys*  AND  comp* )  OR  AFFIL ( dep*  AND  comput* )  OR  AFFIL ( eisc ) )  AND  ( AFFIL ( universidad  AND  del  AND  valle )  OR  AF-ID ( "Universidad del Valle"  60066812 ) ) ')
        '''self.consultas.append('AUTHOR-NAME(AUTHLASTNAME(aranda) AUTHFIRST(j)) AND '+UNIVERSIDAD)
        self.consultas.append('(AUTHOR-NAME(AUTHLASTNAME(diaz) AUTHFIRST(f)) AND NOT (AUTHLASTNAME(diaz) AUTHFIRST(fernando)) ) AND '+UNIVERSIDAD)
        self.consultas.append('AUTHOR-NAME(AUTHLASTNAME(banon) AUTHFIRST(j)) AND '+UNIVERSIDAD)
        self.consultas.append('AUTHOR-NAME(AUTHLASTNAME(bedoya) AUTHFIRST(o)) AND '+UNIVERSIDAD)
        self.consultas.append('AUTHOR-NAME(AUTHLASTNAME(gaona) AUTHFIRST(m)) AND '+UNIVERSIDAD)
        self.consultas.append('AUTHOR-NAME(AUTHLASTNAME(florian) AUTHFIRST(b)) AND '+UNIVERSIDAD)
        self.consultas.append('AUTHOR-NAME(AUTHLASTNAME(solarte) AUTHFIRST(o)) AND '+UNIVERSIDAD)
        self.consultas.append('(AUTHOR-NAME(AUTHLASTNAME(gutierrez) AUTHFIRST(r.e)) OR AUTHOR-NAME(AUTHLASTNAME(pinerez) AUTHFIRST(r))) AND '+UNIVERSIDAD)
        self.consultas.append('((AUTHOR-NAME(AUTHLASTNAME(millan) AUTHFIRST(m)) AND NOT (AUTHLASTNAME(millan) AUTHFIRST(mauricio)) ) OR AUTHOR-NAME(AUTHLASTNAME(millan) AUTHFIRST(s))) AND '+UNIVERSIDAD)
        self.consultas.append('AUTHOR-NAME(AUTHLASTNAME(moreno) AUTHFIRST(p)) AND '+UNIVERSIDAD)
        self.consultas.append('AUTHOR-NAME(AUTHLASTNAME(tischer) AUTHFIRST(i)) AND '+UNIVERSIDAD)
        self.consultas.append('AUTHOR-NAME(AUTHLASTNAME(trujillo) AUTHFIRST(m)) AND '+UNIVERSIDAD)
        self.consultas.append('AUTHOR-NAME(AUTHLASTNAME(carrillo) AUTHFIRST(p)) AND '+UNIVERSIDAD)
        self.consultas.append('AUTHOR-NAME(AUTHLASTNAME(banos) AUTHFIRST(a)) AND '+UNIVERSIDAD)
        self.consultas.append('AUTHOR-NAME(AUTHLASTNAME(villegas) AUTHFIRST(m)) AND '+UNIVERSIDAD)'''

        aranda = '(AUTHOR-NAME(AUTHLASTNAME(aranda) AUTHFIRST(j)) AND '+UNIVERSIDAD
        diaz = '((AUTHOR-NAME(AUTHLASTNAME(diaz) AUTHFIRST(f)) AND NOT (AUTHLASTNAME(diaz) AUTHFIRST(fernando)) ) AND '+UNIVERSIDAD
        banon = '(AUTHOR-NAME(AUTHLASTNAME(banon) AUTHFIRST(j)) AND '+UNIVERSIDAD
        bedoya = '(AUTHOR-NAME(AUTHLASTNAME(bedoya) AUTHFIRST(o)) AND '+UNIVERSIDAD
        gaona = '(AUTHOR-NAME(AUTHLASTNAME(gaona) AUTHFIRST(m)) AND '+UNIVERSIDAD
        florian = '(AUTHOR-NAME(AUTHLASTNAME(florian) AUTHFIRST(b)) AND '+UNIVERSIDAD
        solarte = '(AUTHOR-NAME(AUTHLASTNAME(solarte) AUTHFIRST(o)) AND '+UNIVERSIDAD
        gutierrez = '((AUTHOR-NAME(AUTHLASTNAME(gutierrez) AUTHFIRST(r.e)) OR AUTHOR-NAME(AUTHLASTNAME(pinerez) AUTHFIRST(r))) AND '+UNIVERSIDAD
        millan = '(((AUTHOR-NAME(AUTHLASTNAME(millan) AUTHFIRST(m)) AND NOT (AUTHLASTNAME(millan) AUTHFIRST(mauricio)) ) OR AUTHOR-NAME(AUTHLASTNAME(millan) AUTHFIRST(s))) AND '+UNIVERSIDAD
        moreno = '(AUTHOR-NAME(AUTHLASTNAME(moreno) AUTHFIRST(p)) AND '+UNIVERSIDAD
        tischer = '(AUTHOR-NAME(AUTHLASTNAME(tischer) AUTHFIRST(i)) AND '+UNIVERSIDAD
        trujillo = '(AUTHOR-NAME(AUTHLASTNAME(trujillo) AUTHFIRST(m)) AND '+UNIVERSIDAD
        banos = '(AUTHOR-NAME(AUTHLASTNAME(banos) AUTHFIRST(a)) AND '+UNIVERSIDAD
        carrillo = '(AUTHOR-NAME(AUTHLASTNAME(carrillo) AUTHFIRST(p)) AND '+UNIVERSIDAD
        villegas = '(AUTHOR-NAME(AUTHLASTNAME(villegas) AUTHFIRST(m)) AND '+UNIVERSIDAD
        a = ' OR '
        self.profesores = '(('+aranda+a+diaz+a+banon+a+bedoya+a+gaona+a+florian+a+solarte+a+gutierrez+a+millan+a+moreno+a+tischer+a+trujillo+a+banos+a+carrillo+a+villegas+')'
        #resto_busqueda = '( ISSN ( 0121-5299 )  OR  ISSN ( 0123-3033 )  OR  ISSN ( 1571-0661 )  OR  ISSN ( 0302-9743 )  OR  ISSN ( 2010-3700 )  OR  ISSN ( 1900-8260 )  OR  ISSN ( 0716-8756 )  OR  ISSN ( 0120678 )  OR  ISSN ( 1657-7663 )  OR  ISSN ( 0718-0764 )  OR  ISSN ( 1794-1237 )  OR  ISSN ( 0010-4825 )  OR  ISSN ( 1657-4583 )  OR  ISSN ( 0717-5000 )  OR  ISSN ( 1383-7133 )  OR  ISSN ( 1657-2831 )  OR  ISSN ( 1571-5736 )  OR  ISSN ( 0124-2253 )  OR  ISSN ( 12345 )  OR  ISSN ( 0122-8242 )  OR  ISSN ( 0121-0777 )  OR  ISSN ( 0120-5609 )  OR  ISSN ( 1939-1382 )  OR  ISSN ( 1138-7386 )  OR  ISSN ( 0122-820x )  OR  ISSN ( 0232-0274 )  OR  ISSN ( 0036-1399 )  OR  ISSN ( 1657-5636 )  OR  ISSN ( 0884-8173 )  OR  ISSN ( 0120-548x )  OR  ISSN ( 0121-0262 )  OR  ISSN ( 0031-0603 )  OR  ISSN ( 1676-5680 )  OR  ISSN ( 0234-6206 )  OR  ISSN ( 0218-0014 )  OR  ISSN ( 1909-0056 )  OR  ISSN ( 0012-7353 )  OR  ISSN ( 1553-7358 ) )  OR  ( AFFIL ( ing*  AND  sist*  AND  comp* )  OR  AFFIL ( eng*  AND  sys*  AND  comp* )  OR  AFFIL ( dep*  AND  comput* )  OR  AFFIL ( eisc ) )'
        self.revistas = '( ISSN ( 0121-5299 )  OR  ISSN ( 0123-3033 )  OR  ISSN ( 1571-0661 )  OR  ISSN ( 0302-9743 )  OR  ISSN ( 2010-3700 )  OR  ISSN ( 1900-8260 )  OR  ISSN ( 0716-8756 )  OR  ISSN ( 0120678 )  OR  ISSN ( 1657-7663 )  OR  ISSN ( 0718-0764 )  OR  ISSN ( 1794-1237 )  OR  ISSN ( 0010-4825 )  OR  ISSN ( 1657-4583 )  OR  ISSN ( 0717-5000 )  OR  ISSN ( 1383-7133 )  OR  ISSN ( 1657-2831 )  OR  ISSN ( 1571-5736 )  OR  ISSN ( 0124-2253 )  OR  ISSN ( 12345 )  OR  ISSN ( 0122-8242 )  OR  ISSN ( 0121-0777 )  OR  ISSN ( 0120-5609 )  OR  ISSN ( 1939-1382 )  OR  ISSN ( 1138-7386 )  OR  ISSN ( 0122-820x )  OR  ISSN ( 0232-0274 )  OR  ISSN ( 0036-1399 )  OR  ISSN ( 1657-5636 )  OR  ISSN ( 0884-8173 )  OR  ISSN ( 0120-548x )  OR  ISSN ( 0121-0262 )  OR  ISSN ( 0031-0603 )  OR  ISSN ( 1676-5680 )  OR  ISSN ( 0234-6206 )  OR  ISSN ( 0218-0014 )  OR  ISSN ( 1909-0056 )  OR  ISSN ( 0012-7353 )  OR  ISSN ( 1553-7358 ) )'+UNIVERSIDAD_sin_cerrar_parantesis
        self.direccion = '( AFFIL ( ing*  AND  sist*  AND  comp* )  OR  AFFIL ( eng*  AND  sys*  AND  comp* )  OR  AFFIL ( dep*  AND  comput* )  OR  AFFIL ( eisc ) )'+UNIVERSIDAD_sin_cerrar_parantesis
        conceptos = '(TITLE-ABS-KEY(Constraint theory) OR TITLE-ABS-KEY(Problem solving) OR TITLE-ABS-KEY(Constraint programming) OR TITLE-ABS-KEY(Computer programming languages) OR TITLE-ABS-KEY(Logic programming) OR TITLE-ABS-KEY(Random access storage) OR TITLE-ABS-KEY(Computational geometry) OR TITLE-ABS-KEY(Collision detection) OR TITLE-ABS-KEY(Automatic translation) OR TITLE-ABS-KEY(Classification) OR TITLE-ABS-KEY(Software design) OR TITLE-ABS-KEY(User interfaces) OR TITLE-ABS-KEY(E-learning) OR TITLE-ABS-KEY(Virtual learning environment) OR TITLE-ABS-KEY(Adaptive evaluation) OR TITLE-ABS-KEY(Engineering education) OR TITLE-ABS-KEY(Learning system) OR TITLE-ABS-KEY(Recommender system) OR TITLE-ABS-KEY(Information retrieval) OR TITLE-ABS-KEY(Controlled natural language) OR TITLE-ABS-KEY(statistical parsing) OR TITLE-ABS-KEY(Data mining) OR TITLE-ABS-KEY(Database system) OR TITLE-ABS-KEY(Graph data model) OR TITLE-ABS-KEY(Decision support systems) OR TITLE-ABS-KEY(Graph theory) OR TITLE-ABS-KEY(Knowledge discovery in databases) OR TITLE-ABS-KEY(Recommender systems) OR TITLE-ABS-KEY(Electronic commerce) OR TITLE-ABS-KEY(DNA sequence) OR TITLE-ABS-KEY(Gene cluster) OR TITLE-ABS-KEY(Gene function) OR TITLE-ABS-KEY(Nucleotide sequence) OR TITLE-ABS-KEY(Chromosome map) OR TITLE-ABS-KEY(Computational Biology) OR TITLE-ABS-KEY(Bioinformatics) OR TITLE-ABS-KEY(Cellular automata) OR TITLE-ABS-KEY(Protein folding) OR TITLE-ABS-KEY(Computer vision) OR TITLE-ABS-KEY(Quantitative evaluation) OR TITLE-ABS-KEY(Stereo correspondence) OR TITLE-ABS-KEY(Stereo vision) OR TITLE-ABS-KEY(3D reconstruction) OR TITLE-ABS-KEY(Image coding) OR TITLE-ABS-KEY(Image segmentation) OR TITLE-ABS-KEY(Motion estimation) OR TITLE-ABS-KEY(Stereo correspondence) OR TITLE-ABS-KEY(Histology images) OR TITLE-ABS-KEY(Image analysis))'
        social_semantic = '%s AND %s'%(self.profesores,conceptos)
        #resto_busqueda = '%s OR %s OR %s'%(self.profesores, revistas, self.direccion)
        #busqueda_inicial= profesores+resto_busqueda
        #self.consultas.append('heart')
        #self.consultas.append(busqueda_inicial)
        #self.consultas.append('AUTHOR-NAME(AUTHLASTNAME(aranda) AUTHFIRST(j)) AND '+UNIVERSIDAD)
        '''self.consultas.append('TITLE-ABS-KEY(Constraint theory) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Problem solving) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Constraint programming) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Computer programming languages) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Logic programming) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Random access storage) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Computational geometry) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Collision detection) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Automatic translation) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Classification) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Software design) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(User interfaces) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(E-learning) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Virtual learning environment) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Adaptive evaluation) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Engineering education) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Learning system) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Recommender system) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Information retrieval) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Controlled natural language) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(statistical parsing) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Data mining) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Database system) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Graph data model) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Decision support systems) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Graph theory) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Knowledge discovery in databases) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Recommender systems) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Electronic commerce) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(DNA sequence) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Gene cluster) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Gene function) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Nucleotide sequence) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(chaos) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Chromosome map) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Computational Biology) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Bioinformatics) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Cellular automata) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Protein folding) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Computer vision) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Quantitative evaluation) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Stereo correspondence) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Stereo vision) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(3D reconstruction) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Image coding) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Image segmentation) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Motion estimation) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Histology images) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Genetic algorithms) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(Image analysis) AND '+UNIVERSIDAD)
        self.consultas.append('TITLE-ABS-KEY(CCS) AND '+UNIVERSIDAD)

        self.consultas.append("AUTHOR-NAME ( banon, AND j ) AND "+UNIVERSIDAD)
        self.consultas.append("AUTHOR-NAME(bedoya, AND o) AND "+UNIVERSIDAD)
        self.consultas.append("AUTHOR-NAME(gaona, m) AND "+UNIVERSIDAD)
        self.consultas.append("AUTHOR-NAME(florian, b) AND "+UNIVERSIDAD)
        self.consultas.append("AUTHOR-NAME(solarte, o) AND "+UNIVERSIDAD)
        self.consultas.append("(AUTHOR-NAME(gutierrez, r.e) OR AUTHOR-NAME(pinerez, r)) AND "+UNIVERSIDAD)
        self.consultas.append("((AUTHOR-NAME(millan, m) AND NOT AUTHOR-NAME(millan, mauricio)) OR AUTHOR-NAME(millan, s)) AND "+UNIVERSIDAD)
        self.consultas.append("AUTHOR-NAME(moreno, p) AND "+UNIVERSIDAD)
        self.consultas.append("AUTHOR-NAME(tischer, i) AND "+UNIVERSIDAD)
        self.consultas.append("AUTHOR-NAME(trujillo, m) AND "+UNIVERSIDAD)
        self.consultas.append("AUTHOR-NAME(carrillo, p) AND "+UNIVERSIDAD)
        self.consultas.append("AUTHOR-NAME(banos, a) AND "+UNIVERSIDAD)
        self.consultas.append("AUTHOR-NAME(villegas, m) AND "+UNIVERSIDAD)
        self.consultas.append('AFFIL( ing* AND sist* AND comp*) AND '+UNIVERSIDAD)
        self.consultas.append('AFFIL( eng* AND sys* AND comp*) AND '+UNIVERSIDAD)
        self.consultas.append('AFFIL( dep* AND comput*) AND '+UNIVERSIDAD)
        self.consultas.append('AFFIL(eisc) AND '+UNIVERSIDAD)

        self.consultas.append('ISSN( 0121-5299) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0123-3033) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(1571-0661) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0302-9743) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(2010-3700) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(1900-8260) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0716-8756 ) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0120678) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(1657-7663) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0718-0764) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(1794-1237) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0010-4825) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(1657-4583) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0717-5000) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(1383-7133) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(1657-2831 ) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(1571-5736) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0124-2253) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(12345) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0122-8242) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0121-0777) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0120-5609) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(1939-1382) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(1138-7386) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0122-820X) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0232-0274) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0036-1399) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(1657-5636) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0884-8173) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0120-548X) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0121-0262) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0031-0603) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(1676-5680) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0234-6206) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0218-0014) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(1909-0056) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(0012-7353) AND '+UNIVERSIDAD)
        self.consultas.append('ISSN(1553-7358) AND '+UNIVERSIDAD)'''
    #print self.consultas
    def escribir_resultados(self):
        for i, consulta in enumerate(self.consultas):
            d = Descarga(consulta)
            #print d.construir_peticion()
            self.escribir_resultado(d.obtener_respuesta(d.peticion), str(i+1))

    def escribir_resultado(self, respuesta, nombre_resultado):
        resultado = open('Conceptos/bi'+nombre_resultado+'.csv', 'w')
        tree = ET.parse(respuesta)
        root = tree.getroot()
        for child in root:
            for eid in child.findall('{http://www.w3.org/2005/Atom}eid'):
                print eid.text
                resultado.write(eid.text.strip()+'\n')

    def obtener_eid_100(self, respuesta):
        eids = []
        tree = ET.parse(respuesta)
        root = tree.getroot()
        for child in root:
            for eid in child.findall('{http://www.w3.org/2005/Atom}eid'):
                print eid.text
                eids.append(eid.text.strip())
        return eids

    def descargar_paper(self, doi, user, proyecto):
        d = Descarga(doi)
        d.buscar_por_doi()
        titulo_eid =d.descargar(REPOSITORY_DIR+'%s.%s/'%(user,proyecto))
        return titulo_eid



    def descargar_papers(self, query, cantidad_recuperados, user, proyecto):

        iteraciones = cantidad_recuperados/100
        for i in range(iteraciones):

            d = Descarga(query, i*100)
            xml = d.obtener_respuesta(d.peticion)
            d.descargar_xml(xml, REPOSITORY_DIR+'%s.%s/busqueda'%(user,proyecto)+str(i))
            respuesta = d.obtener_respuesta(d.peticion)
            tree = ET.parse(respuesta)
            root = tree.getroot()

            for child in root:
                for doi in child.findall('{http://prismstandard.org/namespaces/basic/2.0/}doi'):
                    print doi.text
                    titulo_eid = self.descargar_paper(doi.text, user, proyecto)
                    eid = titulo_eid[0]
                    #print 'TIT', titulo
                    titulo = titulo_eid[1]
                    #print 'EIDx', eid
                    if (titulo != ''):
                        self.titulos_descargas.append(titulo)
                        self.eids_descargas.append(eid)
                        self.lista_docs.append(titulo + ".pdf")


    def obtener_metadatos(self, xml, campo):
        respuesta = []
        tree = ET.parse(xml)
        root = tree.getroot()
        for child in root:
            for campito in child.findall(campo):
                print campito.text, campito.tag
                respuesta.append(campito.text)
        return respuesta

    def imprimir_metadatos(self, query):
        d = Descarga(query)
        xml = d.obtener_respuesta(d.peticion)
        print self.obtener_metadatos(xml, '{http://purl.org/dc/elements/1.1/}title')

    def escribir_eid(self, cantidad_recuperados):
        iteraciones = cantidad_recuperados/100
        for i in range(iteraciones):
            print i
            d = Descarga(self.consultas[0],(i*100)+1)
            xml = d.obtener_respuesta(d.peticion)
            print 'ya descargo'
            d.descargar_xml(xml,'xml'+str(i))
            print 'ya escribio'
            self.escribir_resultado(d.obtener_respuesta(d.peticion), str(i+1))

    def obtener_eid(self, cantidad_recuperados, consulta):
        iteraciones = cantidad_recuperados/100
        eids = []
        for i in range(iteraciones):
            print i
            d = Descarga(consulta,(i*100))
            ##xml = d.obtener_respuesta(d.peticion)
            print 'ya descargo'
            #d.descargar_xml(xml,'xml'+str(i))
            print 'ya escribio'
            eids = eids + self.obtener_eid_100(d.obtener_respuesta(d.peticion))
            ##eids = eids + self.obtener_eid_100(open('busqueda1.xml'))
        return eids

    def escribir_docs(self, user, proyecto):
        pdfs = open(REPOSITORY_DIR + str(user) + "." + str(proyecto) + "/" + "docs.txt", "a")
        for pdf in self.lista_docs:
            if pdf is not None:
                pdfs.write(pdf.encode('UTF8') + '\n')
        pdfs.close()


def main():
    ac = AdministradorConsultas()
    #ac.escribir_resultados()
    #ac.escribir_eid(500)
    #ac.descargar_papers('AUTHOR-NAME(AUTHLASTNAME(aranda) AUTHFIRST(j)) AND ( AFFIL ( universidad  AND  del  AND  valle )  OR  AF-ID ( "Universidad del Valle"  60066812 ) )')
    #ac.descargar_papers('Synthesis of novel thiazole-based 8,9-dihydro')
    ac.descargar_papers(ac.profesores, 500, 'cesar', 2)
    #consulta = raw_input('Buscar: ')
    #print consulta
    #ac.descargar_papers(consulta)
    #ac.imprimir_metadatos('computer science')
    #print ac.obtener_eid(100, 'hola')
    print ac.titulos_descargas

#main()
