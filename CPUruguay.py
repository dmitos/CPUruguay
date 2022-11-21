import requests


def GetPostalCodes(dep='MONTEVIDEO', loc='MONTEVIDEO', calle):
    """
    Obtengo datos de codigos postales.

    ***
    """
    DATOS = {'departamento':dep, 'localidad':loc, 'direccion':calle}
    RESP = requests.post('http://geo.correo.com.uy/serviciosv2/CodigoPostal', data=DATOS)
    contenido = json.loads(RESP.content.decode("utf-8"))
    for info in contenido:
        return info["codigoPostal"]
