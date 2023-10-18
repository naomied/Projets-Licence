<%@ page import="java.sql.*,java.util.List,java.util.ArrayList, connexion.*, bdd.*, client.*" %>

<html>
    <head>
        <title>Sports/Lieu</title>
        <link rel="stylesheet" type="text/css" href="css/Style.css">
      </head>
  <body>
    <nav> 
        <div class="navbar" id="navbar">
            <div class="menu"> 
                <a class="nav-link" href="Pays.jsp">Pays Participants</a>
                <a class="nav-link-active" href="Site.jsp">Sites</a>
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
                <a class="nav-link" href="DetenteurRecord.jsp">Detenteurs de records</a>
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
    //On recupere les valeurs des input
    String jour = request.getParameter("jour").trim();
    String mois = request.getParameter("mois").trim();
    String laDate = jour+"-"+mois+"-"+"2024";
    Fonction f = new Fonction();
    Connection con = null;
    Deconnexion decon = new Deconnexion();
    BDTable bd = new BDTable();
    SessionJO site = new SessionJO();
    Connexion c = null;
    
    try {
        c = new Connexion();
        c.connecter();
        con = c.getCon();
        java.sql.Statement stmt = con.createStatement();
        String requete = "select id_Session,num_jour_Session,date_Session,heure_debut,heure_fin,nom_sport_jo,nom_site from Session INNER JOIN Sport_jo USING(id_sport_jo) INNER JOIN Site USING(id_site) where date_session ='" + laDate + "' UNION select id_Session,num_jour_Session,date_Session,heure_debut,heure_fin,nom_sport_jp,nom_site from Session INNER JOIN Sport_jp USING(id_sport_jp) INNER JOIN Site USING(id_site) where date_session ='" + laDate +"'";
        BDTable[] lSite = f.findWthReq(requete, site, con);
        SessionJO [] listeSess  = new SessionJO[lSite.length];
        out.println("<div class='table-wrapper'>");
            out.println("<table class ='fl-table'>");
                out.println("<tr><th>Nom du sport</th></tr>");
                for (int i = 0; i < lSite.length; i++) {
                listeSess[i]= (SessionJO) lSite[i];
                out.println("<tr><td>" + listeSess[i].getId_Sport_JO()+"</td></tr>");
          }
          out.println("</table>");
          out.println("</div>");
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