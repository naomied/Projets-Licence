<%@ page import="java.sql.*, connexion.*, bdd.*, client.*" %>
<html>
  <head>
    <title>Les détenteurs de record par épreuves</title>
    <link rel="stylesheet" type="text/css" href="/css/Style.css">
  </head>
  <body>
  <nav> 
    <div class="navbar" id="navbar">
        <div class="menu"> 
            <a class="nav-link" href="Pays.jsp">Pays Participants</a>
            <a class="nav-link" href="Site.jsp">Sites</a>
            <div class="dropdown-simple">
                <a class="nav-link" href="#">Sports</a>
                <div class="dropdown-content">
                    <div class="dropdown-row">
                        <div class="dropdown-column">
                            <ul>
                                <li><a href="Sport_Jo.jsp">Sports Olympiques</a></li>
                            </ul>
                        </div>
                        <div class="dropdown-column">
                            <ul>
                                <li><a href="Sport_Jp.jsp">Sports Paralympiques</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="dropdown-simple">
                <a class="nav-link" href="#">Sessions</a>
                <div class="dropdown-content">
                    <div class="dropdown-row">
                        <div class="dropdown-column">
                            <ul>
                                <li><a href="Session_JO.jsp">Sessions Olympiques</a></li>
                            </ul>
                        </div>
                        <div class="dropdown-column">
                            <ul>
                                <li><a href="Session_JP.jsp">Sessions Paralympiques</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <a class="nav-link" href="Epreuve.jsp">Epreuves</a>
            <a class="nav-link-active" href="DetenteurRecord.jsp">Detenteurs de records</a>
            <a class="nav-link" href="Recherche.jsp">RECHERCHE AVANCEE</a>

        </div>
        <div class="search-bar"> 
            <form class="search-bar-form">

                <input class="search-bar-input"  type="search" onfocusout="this.value=''" placeholder="Rechercher..."  autocomplete="off" required><i class="fa fa-search" ></i>

                <div id="suggestions"></div>

            </form>

        </div>

    </div>

    </nav>
    <div class = "fond">
        <img src="/css/fond.png" alt="">
    </div>
    <%
        Fonction f = new Fonction();
        Connection con = null;
        Deconnexion decon = new Deconnexion();
        BDTable bd = new BDTable();
        Detenteur_Record det = new Detenteur_Record();
        Connexion c = null;
        try {
            System.out.println("tafiditra anaty try");
            c = new Connexion();
            c.connecter();
            con = c.getCon();
            java.sql.Statement stmt = con.createStatement();
            System.out.println("tonga");

            String requete = "select id_detenteur_record,nom_detenteur_record,prenom_detenteur_record,date_naissance,nom_epreuve from detenteur_record as det,epreuve where det.id_epreuve = epreuve.id_epreuve";
            System.out.println(requete);
            BDTable[] ldet = f.findWthReq(requete, det, con);

            Detenteur_Record[] listedet = new Detenteur_Record[ldet.length];
            
            out.println("<div class='table-wrapper'>");
                out.println("<table class ='fl-table'>");
                    out.println("<tr><th>ID</th><th>Nom et Prenom</th><th>Date de Naissance</th><th>Epreuve</th></tr>");
                 for (int i = 0; i < ldet.length; i++) {
                    listedet[i] = (Detenteur_Record) ldet[i];
                    out.println("<tr><td>" + listedet[i].getId_Detenteur_Record() +  "</td><td>" + 
                        listedet[i].getNom_Detenteur_Record() + " " + listedet[i].getPrenom_Detenteur_Record() + "</td><td>" + 
                        listedet[i].getDate_naissance() + "</td><td>"+
                        listedet[i].getId_Epreuve() + "</td></tr>");
              }
              out.println("</table>");
              out.println("</div>");
        } catch (SQLException e1) {
            out.println(e1.getMessage());
            if (c.getCon() != null) {
                con.rollback();
            }
        } catch (Exception e2) {
            out.println(e2.getMessage());
        } finally {
            if (c.getCon() != null) {
                decon.deconnect(c);
            }
        }
    %>
  </body>
</html>