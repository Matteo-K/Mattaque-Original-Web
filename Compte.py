import mysql.connector
from mysql.connector import errorcode

# Caractéristiques de la connection
database    = 'compte'
host_ip     = '127.0.0.1'
utilisateur = 'root'
password    = ''

#####################
# CONNECTION à la BDD
#####################
try:   
  conn = mysql.connector.connect(
      user = utilisateur, 
      password = password,
      host = host_ip,
      database = database)

#################################
# la connection à la BDD a échoué   
#################################
except mysql.connector.Error as err:    

    # Si Erreur de nom d'utilisateur ou de mot de passe
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Votre nom d'utilisateur ou votre mot de passe ne correspond pas !")

    # Si Erreur de nom de base de donnÃ©es
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de données",database,"n'existe pas")
    # Si autre Erreur
    else:
        print(err)

#################################
# La connection à  la BDD a réussi 
#################################
else:         
    print("vous êtes connecté à la base", conn._database)

##################################################################  
# On créé un curseur MySQL qui contient le rÃ©sultat de la requête
##################################################################
    curseur = conn.cursor(buffered=True)


def select_id_max () :
    """
    Sélectionne l'identifiant le plus élevée parmis la base de données

    Returns
    -------
    int
        l'identifiant max de la table connexion.

    """
    requete=("SELECT MAX(id_utilisateur) FROM connexion;")
    curseur.execute(requete)
    return curseur.fetchall()[0][0]


def créer_compte (id_user : int, Mail : str, MDP : str, Nom_user : str):
    """
    Créer un nouveau compte à l'utilisateur

    Parameters
    ----------
    id_user : int
        Identifiant de l'utilisateur.
    Mail : str
        Mail de l'utilisateur.
    MDP : str
        Mot de passe de l'utilisateur.
    Nom_user : str
        Nom de l'utilisateur.

    """
    requete=("INSERT INTO utilisateur (id,Nom_Compte_Utilisateur,Nombre_Connexion) VALUES ('"+ str(id_user) +"','"+ str(Nom_user) +"','"+ str(0) +"');")
    curseur.execute(requete)
    conn.commit()
    requete=("INSERT INTO connexion (id_utilisateur,Mail,Mot_De_Pass) VALUES ('"+ str(id_user) +"','"+ str(Mail) +"','"+ str(MDP) +"');")
    curseur.execute(requete)
    conn.commit()
    
def nv_connexion (id_user : int):
    """
    Implémente une connexion en plus à l'utilisateur

    Parameters
    ----------
    id_user : int
        Idetifiant de l'utilisateur.
    """
    #recherche le nombre de connexion de l'utilisateur
    requete=("SELECT Nombre_Connexion FROM utilisateur WHERE id= '"+ str(id_user) +"';")
    curseur.execute(requete)
    nb_connexion = curseur.fetchall()[0][0]
    
    #ajoute une connexion à celle de l'utilisateur
    requete=("UPDATE utilisateur SET Nombre_Connexion='"+ str(nb_connexion+1) +"' WHERE id='"+ str(id_user) +"';")
    curseur.execute(requete)
    conn.commit()   # Les modifications sont appliqués dans la BDD


#exemple d'utilisation
#créer_compte(int(input("Numéro d'identifiant ")), input("Le mail "), input("Le mot de passe "), input("Le nom d'utilisateur "))