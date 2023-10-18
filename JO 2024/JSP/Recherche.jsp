<%@ page import="java.sql.*,java.util.List,java.util.ArrayList, connexion.*, bdd.*, client.*" %>
<%
        Fonction f = new Fonction();
        Connection con = null;
        Deconnexion decon = new Deconnexion();
        BDTable bd = new BDTable();
        Site site = new Site();
        Connexion c = null;
        List<Site> listeSite = new ArrayList<Site>();
        try {
            System.out.println("tafiditra anaty try");
            c = new Connexion();
            c.connecter();
            con = c.getCon();
            java.sql.Statement stmt = con.createStatement();
            System.out.println("tonga");

            String requete = "select * from Site";
            System.out.println(requete);
            BDTable[] lSite = f.findWthReq(requete, site, con);

            for (int i = 0; i < lSite.length; i++) {
                listeSite.add((Site) lSite[i]);
            }
            
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
<html>
    <head>
        <title>Sites</title>
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
                <a class="nav-link" href="#">RECHERCHE AVANCEE</a>
    
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
        <div class="containerRecherche">
            <div class="search-site">
                <h1> Recherche de transports par site</h1>
                <h2> Trouver les transports qui mennent au site:</h2>
                <form action="chercheTransport.jsp" method="get">
                    <label  for="site">Choisir un site:</label>
                    <select id="site" name="nom-site" size="3">
                        <% for(int i=0; i<listeSite.size(); i++) { %>
                            <option value="<%= listeSite.get(i).getNom_Site() %>">
                                <%= listeSite.get(i).getNom_Site() %>
                            </option>
                        <% } %>
                    </select>
                    <br/>
                    <input type="submit" value="RECHERCHER"></p>
                </form>
            </div>
            <div class="search-site">
                <h1> Recherche des sports par Date</h1>
                <h2> Trouver les sports qui ont lieu le:</h2>
                <form action="chercheSportJour.jsp" method="get">
                    <label for="jour">Jour:</label>
                    <select id="jour" name="jour">
                      <option value="">Choisir un jour</option>
                      <% for(int i = 1; i <= 31; i++) { %>
                        <option value="<%= i %>"><%= i %></option>
                      <% } %>
                    </select>
                    
                    <label for="mois">Mois:</label>
                    <select id="mois" name="mois">
                      <option value="">Choisir un mois</option>
                      <% for(int i = 7; i <= 9; i++) { %>
                        <option value="<%= i %>"><%= i %></option>
                      <% } %>
                    </select>
                    

                    <input type="submit" value="RECHERCHER"></p>
                </form>
            </div>
            
        </div>
  </body>
</html>