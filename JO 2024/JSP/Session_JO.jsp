<%@ page import="java.sql.*, connexion.*, bdd.*, client.*" %>
<html>
  <head>
    <title>Sessions Olympiques</title>
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
                  <a class="nav-link-active" href="#">Sessions</a>
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
        Fonction f = new Fonction();
        Connection con = null;
        Deconnexion decon = new Deconnexion();
        BDTable bd = new BDTable();
        SessionJO sess = new SessionJO();
        Connexion c = null;
        try {
            System.out.println("tafiditra anaty try");
            c = new Connexion();
            c.connecter();
            con = c.getCon();
            java.sql.Statement stmt = con.createStatement();
            System.out.println("tonga");

            String requete = "select id_Session,num_jour_Session,date_Session,heure_debut,heure_fin,nom_sport_jo,nom_site from Session INNER JOIN Sport_jo USING(id_sport_jo) INNER JOIN Site USING(id_site)";
            BDTable[] lSessionJO = f.findWthReq(requete, sess, con);
            
            SessionJO[] listeSessionJO = new SessionJO[lSessionJO.length];
            
            out.println("<div class='table-wrapper'>");
              out.println("<table class ='fl-table'>");
                    out.println("<tr><th>ID</th><th>Num Jour SessionJO</th><th>Date</th><th>Heure Debut</th><th>Heure Fin</th><th>Sport</th><th>Site</th></tr>");
                 for (int i = 0; i < lSessionJO.length; i++) {
                    listeSessionJO[i] = (SessionJO) lSessionJO[i];
                    out.println("<tr><td>" + listeSessionJO[i].getId_Session() + "</td><td>"+
                    listeSessionJO[i].getNum_Jour_Session()+ "</td><td>" + listeSessionJO[i].getDate_Session() + "</td><td>"+
                    listeSessionJO[i].getHeure_Debut()+ "</td><td>" + listeSessionJO[i].getHeure_Fin() +"</td><td>"+
                    listeSessionJO[i].getId_Sport_JO()+ "</td><td>" + listeSessionJO[i].getId_Site() +
                    "</td><tr>");
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