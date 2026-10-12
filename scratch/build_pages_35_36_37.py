import os

workspace = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF-Miami\IHTF"

def get_template(lang, year, ed_num, plays_html):
    if lang == "es":
        title = f"{ed_num}° Festival Internacional de Teatro Hispano de Miami ({year}) | Archivos"
        desc = f"Programa oficial de obras presentadas en la {ed_num}ª edición del Festival Internacional de Teatro Hispano de Miami ({year})."
        canonical = f"https://vayol-art.github.io/IHTF/es/archivos-del-festival/{year}/"
        en_switch_url = f"../../../en/archivos-del-festival/{year}/"
        header_h2 = f"{ed_num} FESTIVAL INTERNACIONAL DE TEATRO HISPANO DE MIAMI"
        header_p = f"PROGRAMA {year}"
        hero_title = "ARCHIVOS DEL FESTIVAL"
        newsletter_h2 = "Suscríbete a nuestro Newsletter"
        newsletter_p = "Recibe información actualizada sobre el IHTF"
        privacy_label = "Políticas de privacidad"
        terms_label = "Términos y condiciones"
        current_lang_text = "Español"
        home_href = "../../#inicio"
        
        lang_btn_html = f'''          <div class="lang-dropdown">
            <a href="#" class="lang-opt active" onclick="switchLang('es'); return false;">Español</a>
            <a href="{en_switch_url}" class="lang-opt" onclick="switchLang('en', '{en_switch_url}')">English</a>
          </div>'''
        
        lang_switch_script = f'''        langOpts[0].addEventListener("click", function () {{ // Spanish
          localStorage.setItem("preferred_lang", "es");
          langSelector.classList.remove("open");
        }});
        langOpts[1].addEventListener("click", function () {{ // English
          localStorage.setItem("preferred_lang", "en");
          window.location.href = "{en_switch_url}";
        }});'''

        nav_menu_html = '''        <div class="nav-dropdown-wrapper">
          <a href="../../agenda/" class="nav-dropdown-trigger">PROGRAMA</a>
          <div class="nav-submenu">
            <a href="../../agenda/" class="submenu-item">PROGRAMA 2026</a>
            <a href="../../programa-de-mano/" class="submenu-item">Programa de Mano</a>
            <a href="../../calendario/" class="submenu-item">Calendario</a>
            <a href="../../eventos-adicionales/" class="submenu-item">Eventos Adicionales</a>
            <div class="dropdown-divider"></div>
            <a href="../../dia-internacional-del-nino/" class="submenu-item">Día Internacional del Niño</a>
            <a href="../../teatros/" class="submenu-item">Teatros</a>
            <a href="../../sponsors/" class="submenu-item">Apoya IHTF</a>
            <a href="../../archivos-del-festival/" class="submenu-item">Archivos del Festival</a>
          </div>
        </div>
        <a href="../../contactanos/">CONTÁCTANOS</a>
        <div class="nav-dropdown-wrapper">
          <a href="../../nosotros/" class="nav-dropdown-trigger">SOBRE NOSOTROS</a>
          <div class="nav-submenu">
            <a href="../../nosotros/#compania" class="submenu-item">Historia del Festival</a>
            <a href="../../nosotros/#personal" class="submenu-item">Personal</a>
          </div>
        </div>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSczcvvSrHnWwI0TgvGq_Ad9R9uOO-UCv7Eqy5VTrn_HMan4-g/viewform?usp=header" target="_blank">INSCRIPCIONES 41° FESTIVAL</a>'''
        
    else: # English
        suffix = "st" if str(ed_num).endswith("1") else "nd" if str(ed_num).endswith("2") else "rd" if str(ed_num).endswith("3") else "th"
        title = f"{ed_num}{suffix} International Hispanic Theatre Festival of Miami ({year}) | Archives"
        desc = f"Official program of plays presented at the {ed_num}{suffix} International Hispanic Theatre Festival of Miami ({year})."
        canonical = f"https://vayol-art.github.io/IHTF/en/archivos-del-festival/{year}/"
        es_switch_url = f"../../../es/archivos-del-festival/{year}/"
        header_h2 = f"{ed_num}{suffix.upper()} INTERNATIONAL HISPANIC THEATRE FESTIVAL OF MIAMI"
        header_p = f"{year} PROGRAM"
        hero_title = "FESTIVAL ARCHIVES"
        current_lang_text = "English"
        newsletter_h2 = "Subscribe to our Newsletter"
        newsletter_p = "Receive updated information about IHTF"
        privacy_label = "Privacy Policy"
        terms_label = "Terms & Conditions"
        home_href = "../../#inicio"
        
        lang_btn_html = f'''          <div class="lang-dropdown">
            <a href="{es_switch_url}" class="lang-opt" onclick="switchLang('es', '{es_switch_url}')">Español</a>
            <a href="#" class="lang-opt active" onclick="switchLang('en'); return false;">English</a>
          </div>'''
          
        lang_switch_script = f'''        langOpts[0].addEventListener("click", function () {{ // Spanish
          localStorage.setItem("preferred_lang", "es");
          window.location.href = "{es_switch_url}";
        }});
        langOpts[1].addEventListener("click", function () {{ // English
          localStorage.setItem("preferred_lang", "en");
          langSelector.classList.remove("open");
        }});'''

        nav_menu_html = '''        <div class="nav-dropdown-wrapper">
          <a href="../../agenda/" class="nav-dropdown-trigger">PROGRAM</a>
          <div class="nav-submenu">
            <a href="../../agenda/" class="submenu-item">2026 PROGRAM</a>
            <a href="../../programa-de-mano/" class="submenu-item">Program</a>
            <a href="../../calendario/" class="submenu-item">Calendar</a>
            <a href="../../eventos-adicionales/" class="submenu-item">Additional Events</a>
            <div class="dropdown-divider"></div>
            <a href="../../dia-internacional-del-nino/" class="submenu-item">International Children's Day</a>
            <a href="../../teatros/" class="submenu-item">Theatres</a>
            <a href="../../sponsors/" class="submenu-item">Support IHTF</a>
            <a href="../../archivos-del-festival/" class="submenu-item">Festival Archives</a>
          </div>
        </div>
        <a href="../../contactanos/">CONTACT US</a>
        <div class="nav-dropdown-wrapper">
          <a href="../../nosotros/" class="nav-dropdown-trigger">ABOUT US</a>
          <div class="nav-submenu">
            <a href="../../nosotros/#compania" class="submenu-item">History of the Festival</a>
            <a href="../../nosotros/#personal" class="submenu-item">Staff</a>
          </div>
        </div>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSczcvvSrHnWwI0TgvGq_Ad9R9uOO-UCv7Eqy5VTrn_HMan4-g/viewform?usp=header" target="_blank">REGISTRATION 41st FESTIVAL</a>'''

    return f'''<!doctype html>
<html lang="{lang}">
<head>
<!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=AW-17480587494"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());

    gtag('config', 'AW-17480587494');
  </script>
  <link rel="icon" type="image/png" href="../../../assets/favicon.png" />

  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{canonical}" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="https://vayol-art.github.io/IHTF/assets/favicon.png" />
  <meta property="og:locale" content="{"es_US" if lang=="es" else "en_US"}" />
  <meta property="og:site_name" content="{"Festival Internacional de Teatro Hispano de Miami" if lang=="es" else "International Hispanic Theatre Festival of Miami"}" />

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="../../../fonts.css">
  <link rel="stylesheet" href="../../../agenda.css?v=1.0.9">
  <link rel="stylesheet" href="../../../edicion-historica.css?v=1.0.0">

<script>
  function toggleLangDropdown(e) {{
    if (e && typeof e.stopPropagation === 'function') {{
      e.stopPropagation();
    }}
    const btn = (e && e.currentTarget) ? e.currentTarget : document.querySelector(".lang-btn");
    const selector = btn ? btn.closest(".lang-selector") : document.querySelector(".lang-selector");
    if (selector) {{
      const isOpen = selector.classList.toggle("open");
      if (btn) btn.setAttribute("aria-expanded", isOpen);
    }}
  }}

  function switchLang(lang, targetUrl) {{
    localStorage.setItem("preferred_lang", lang);
    if (targetUrl && targetUrl !== "#") {{
      let finalUrl = targetUrl;
      if (window.location.search && targetUrl.includes("/obra/")) {{
        finalUrl += window.location.search;
      }}
      window.location.href = finalUrl;
    }}
  }}

  document.addEventListener("click", function (event) {{
    const selector = document.querySelector(".lang-selector");
    const btn = document.querySelector(".lang-btn");
    if (selector && !selector.contains(event.target)) {{
      selector.classList.remove("open");
      if (btn) btn.setAttribute("aria-expanded", "false");
    }}
  }});
</script>
</head>
<body>
  <header class="site-header">
    <a class="brand" href="{home_href}" aria-label="IHTF Inicio">
      <img class="logo-white" src="../../../assets/LOGO_EXPORTS%202/LOGOS_DIGITAL/Web/logo%20blanco.png" alt="IHTF 40 Blanco" />
      <img class="logo-color" src="../../../assets/LOGO_EXPORTS%202/LOGOS_DIGITAL/Web/logo%20colores.png" alt="IHTF 40 Color" />
    </a>
    <div class="nav-container">
      <nav class="main-nav" aria-label="Menú principal">
{nav_menu_html}
      </nav>

      <div class="header-actions">
        <div class="lang-selector">
          <button class="lang-btn" onclick="toggleLangDropdown(event)" aria-label="Cambiar idioma" aria-expanded="false">
            <svg class="icon-globe" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="2" y1="12" x2="22" y2="12"></line>
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10z"></path>
            </svg>
            <span class="lang-text">{current_lang_text}</span>
            <svg class="icon-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
{lang_btn_html}
        </div>
        <button class="hamburger" aria-label="Abrir menú" aria-expanded="false">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </div>
  </header>

  <main>
    <section class="hero">
      <h1>{hero_title}</h1>
    </section>

    <div class="archive-edition-page">
      <div class="edition-container">
        
        <div class="edition-header-title">
          <h2>{header_h2}</h2>
          <p>{header_p}</p>
        </div>

{plays_html}

      </div>
    </div>
  </main>

  <div class="footer-wrapper">
    <section class="newsletter" id="newsletter">
      <div class="section-inner narrow">
        <h2>{newsletter_h2}</h2>
        <p>{newsletter_p}</p>
        <style>
          .newsletter {{
            padding: 40px 24px 20px !important;
          }}
          .newsletter .section-inner {{
            padding: 25px 30px 20px !important;
          }}
          .newsletter h2 {{
            margin-bottom: 6px !important;
          }}
          .newsletter p {{
            margin: 6px auto 16px !important;
          }}
        </style>

        <!-- Begin Constant Contact Inline Form Code -->
        <div class="ctct-inline-form" data-form-id="6b84846d-b4c9-4b02-867d-09c8a7ac5d40"></div>
        <!-- End Constant Contact Inline Form Code -->
      </div>
    </section>
    <footer class="site-footer">
      <div><img src="../../../assets/LOGO_EXPORTS%202/LOGOS_DIGITAL/Web/logo%20blanco.png" alt="IHTF 40 Blanco" class="footer-logo" /></div>
      <nav><a href="#">{privacy_label}</a><a href="#">{terms_label}</a></nav>
    </footer>
  </div>

  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      const hamburger = document.querySelector(".hamburger");
      const mainNav = document.querySelector(".main-nav");
      if (hamburger && mainNav) {{
        hamburger.addEventListener("click", function(e) {{
          e.stopPropagation();
          const isOpen = hamburger.classList.toggle("open");
          mainNav.classList.toggle("open");
          hamburger.setAttribute("aria-expanded", isOpen);
        }});
        document.addEventListener("click", function(event) {{
          if (!hamburger.contains(event.target) && !mainNav.contains(event.target)) {{
            hamburger.classList.remove("open");
            mainNav.classList.remove("open");
            hamburger.setAttribute("aria-expanded", "false");
          }}
        }});
      }}

      // Language Selector Dropdown logic
      const langSelector = document.querySelector(".lang-selector");
      const langBtn = document.querySelector(".lang-btn");
      if (langSelector && langBtn) {{
        document.addEventListener("click", function (event) {{
          if (!langSelector.contains(event.target)) {{
            langSelector.classList.remove("open");
            langBtn.setAttribute("aria-expanded", "false");
          }}
        }});
      }}

      // Language options click behavior
      const langOpts = document.querySelectorAll(".lang-opt");
      if (langOpts.length >= 2) {{
{lang_switch_script}
      }}

      // Header scroll animation
      const header = document.querySelector('.site-header');
      const hero = document.querySelector('.hero');
      if (header && hero) {{
        const updateHeader = () => {{
          const heroBottom = hero.getBoundingClientRect().bottom;
          if (heroBottom <= 100) {{
            header.classList.add('scrolled');
          }} else {{
            header.classList.remove('scrolled');
          }}
        }};
        window.addEventListener('scroll', updateHeader);
        updateHeader();
      }}
    }});
  </script>
  <!-- Begin Constant Contact Active Forms -->
  <script> var _ctct_m = "a79e89c0998befa80793c5464469c842"; </script>
  <script id="signupScript" src="https://static.ctctcdn.com/js/signup-form-widget/current/signup-form-widget.min.js" async defer></script>
  <!-- End Constant Contact Active Forms -->
</body>
</html>
'''

def build_plays_html(plays, ed_folder):
    html_blocks = []
    for i, p in enumerate(plays, 1):
        thumb_path = f"../../../assets/Fotos_Archivos/{ed_folder}/cropped/Obra{i}.png"
        contact_html = f'''              <div class="play-contact">{p["contact"]}</div>''' if p.get("contact") else ""
        credits_html = f'''              <div class="play-credits">{p["credits"]}</div>''' if p.get("credits") else ""
        dates_html = f'''              <div class="play-dates">{p["dates"]}</div>''' if p.get("dates") else ""
        company_html = f'''              <div class="play-company">{p["company"]}</div>''' if p.get("company") else ""
        venue_html = f'''              <div class="play-venue">{p["venue"]}</div>''' if p.get("venue") else ""
        synopsis_html = f'''              <div class="play-synopsis">{p["synopsis"]}</div>''' if p.get("synopsis") else ""

        block = f'''        <!-- Obra {i} -->
        <article class="play-item">
          <div class="play-top">
            <div class="play-thumb">
              <img src="{thumb_path}" alt="{p["title"]}" loading="lazy" />
            </div>
            <div class="play-meta">
{dates_html}
{company_html}
              <h3 class="play-title">{p["title"]}</h3>
{credits_html}
{synopsis_html}
{venue_html}
{contact_html}
            </div>
          </div>
        </article>'''
        html_blocks.append(block)
    return "\n\n".join(html_blocks)

# ==================== DATA EDICION 35 (2021) ====================
plays_2021_es = [
    {
        "dates": "Jueves 17 de junio | 7:00 P.M.",
        "company": "LEDA ALMAR | Artista (Argentina)",
        "title": "PRESENTACIÓN DEL CARTEL OFICIAL",
        "credits": "Encuentro con la Artista | Recepción y cóctel",
        "synopsis": "Presentación oficial del afiche representativo de la 35ª edición del Festival Internacional de Teatro Hispano de Miami.<br><br>www.ledaalmar.com | @leda.almar.art",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "(Por invitación)"
    },
    {
        "dates": "8 al 25 de julio | Después de cada estreno",
        "company": "DRA. BEATRIZ J. RIZK | Directora del Programa Educativo",
        "title": "COMPONENTE EDUCATIVO | FOROS DE DEBATE",
        "credits": "Espacio de intercambio y diálogo entre creadores y público",
        "synopsis": "Coloquios en español e inglés conducidos inmediatamente al término de cada función de estreno con los elencos, directores y público.",
        "venue": "Salas del Festival | Miami",
        "contact": "Entrada libre con la función"
    },
    {
        "dates": "Jueves 8 de julio | Antes de la función",
        "company": "PREMIO A UNA VIDA DE DEDICACIÓN A LAS ARTES ESCÉNICAS 2021",
        "title": "GRISELDA GAMBARO",
        "credits": "Dramaturga y escritora | Argentina",
        "synopsis": "Entrega del Premio a una Vida de Dedicación a las Artes Escénicas 2021 a la insigne dramaturga y escritora argentina Griselda Gambaro, figura cumbre del teatro latinoamericano universal.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Entrada incluida con la función"
    },
    {
        "dates": "Jueves, Viernes y Sábado, 8, 9 y 10 de julio | 8:30 P.M.<br>Domingo 11 de julio | 5:00 P.M.",
        "company": "COMEDIA NACIONAL | Montevideo, Uruguay",
        "title": "NOCIONES BÁSICAS PARA LA CONSTRUCCIÓN DE PUENTES",
        "credits": "Escrita y dirigida por Jimena Márquez",
        "synopsis": "Tomando las experiencias íntimas de todos los involucrados en la creación de esta obra, dividimos la historia y universo de Mario Benedetti en cinco zonas emocionales: Montevideo, Militancia, Marketing, Exilio...",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Comedia dramática"
    },
    {
        "dates": "Viernes y Sábado, 9 y 10 de julio | 8:30 P.M.<br>Domingo 11 de julio | 5:00 P.M.",
        "company": "MURGA MADRE | Montevideo, Uruguay",
        "title": "MURGA MADRE",
        "credits": "Escrita por Pablo Routin | Dirigida por Fernando Toja | Dirección musical: Edu Lombardo",
        "synopsis": "Silencios. Miradas que dicen lo que no se expresa en palabras. Dos personajes sin nombres, tiempo ni espacio... el retorno a través de la murga. Fragmentos esparcidos para completar una historia. El fluir eterno de la vida. Ayer, hoy y siempre... un espectáculo para el alma.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Teatro musical / Murga"
    },
    {
        "dates": "Jueves, Viernes y Sábado, 15, 16 y 17 de julio | 8:30 P.M.",
        "company": "TEATRO DE LA VUELTA | Cuenca, Ecuador",
        "title": "BARRIO CALEIDOSCOPIO",
        "credits": "Escrita y dirigida por Carlos Gallegos",
        "synopsis": "Alfonsito despierta con deseos de ir a la tienda a comprar pan. Para lograrlo, debe vencer sus múltiples miedos excéntricos, aparentar ser una persona «normal» y salir de su polvoriento hogar. Deberá cruzar la calle sorteando burlas, tristezas y a la maquiavélica Magalita para que su corazón no estalle.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Clown dramático"
    },
    {
        "dates": "Viernes y Sábado, 16 y 17 de julio | 8:30 P.M.<br>Domingo 18 de julio | 5:00 P.M.",
        "company": "TEATRO BOXING / EL GALPÓN | Uruguay",
        "title": "TOM PAIN (basado en nada)",
        "credits": "De Will Eno | Dirigida por Lucio Hernández | Con Rogelio Gracia (Premio Florencio Sánchez)",
        "synopsis": "Un hombre aparentemente ordinario convierte su dolor en provocación. Con honestidad y humor comparte historias de su vida sobre la picadura de una abeja, un niño y un perro, y una mujer.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Monólogo"
    },
    {
        "dates": "Sábado 17 de julio | 5:00 P.M.",
        "company": "COLECTIVO ANIMAL (Colombia) & CONECTA MIAMI ARTS (EE. UU.)",
        "title": "UN BOSQUE ENCANTADO",
        "credits": "Escrita y dirigida por Camila Rivera, Tatiana Samper y Daniel Roa | Dir. Musical: Daniel Roa",
        "synopsis": "Un viaje musical y teatral por el bosque que celebra la naturaleza, los animales y el cuidado del planeta para toda la familia.<br><br>Copresentada por Key Biscayne Community Center.",
        "venue": "Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
        "contact": "Entrada y estacionamiento gratis"
    },
    {
        "dates": "Domingo 18 de julio | 2:00 - 6:00 P.M.",
        "company": "DÍA INTERNACIONAL DEL NIÑO",
        "title": "DÍA INTERNACIONAL DEL NIÑO",
        "credits": "Talleres interactivos de arte y función teatral: «Un bosque encantado»",
        "synopsis": "Gran jornada festiva familiar:<br>• 2:00 – 3:00 P.M.: Manualidades, atracciones y meriendas saludables<br>• 3:00 – 4:00 P.M.: Talleres de Pintura y Títeres<br>• 4:00 – 5:00 P.M.: Talleres de Música y Danza<br>• 5:00 – 6:00 P.M.: Función de teatro «Un bosque encantado» (Colectivo Animal & Conecta Miami Arts)",
        "venue": "MDCA’s Mid-Stage Theatre | 2901 West Flagler Street, Miami",
        "contact": "Entrada y estacionamiento gratis"
    },
    {
        "dates": "Jueves, Viernes y Sábado, 22, 23 y 24 de julio | 8:30 P.M.<br>Domingo 25 de julio | 5:00 P.M.",
        "company": "TEATRO AVANTE | Miami, Florida, EE. UU.",
        "title": "UBÚ PANDEMIA",
        "credits": "De Abel González Melo | Dirigida por Mario Ernesto Sánchez (Estreno Mundial)",
        "synopsis": "En medio de una crisis social sin precedentes, el Rey Ubú se ve forzado a regresar a la isla mítica de Uba, donde sus habitantes se han rebelado. Para colmo, una pandemia azota al mundo y amenaza con entrar a la isla. Convencido de la inmunidad de su pueblo, Ubú desata una insólita campaña... (En español con supertítulos en inglés)",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Estreno mundial"
    },
    {
        "dates": "Viernes y Sábado, 23 y 24 de julio | 8:30 P.M.<br>Domingo 25 de julio | 5:00 P.M.",
        "company": "LOS PINCHES CHAMACOS | CDMX, México",
        "title": "PAPÁ ESTÁ EN LA ATLÁNTIDA",
        "credits": "Escrita por Javier Malpica | Dirigida por Esteban Castellanos",
        "synopsis": "Una conmovedora historia de orfandad y lealtad mutua entre dos hermanos que emprenden un viaje lleno de vicisitudes para reencontrarse con su padre en los Estados Unidos.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Drama"
    }
]

plays_2021_en = [
    {
        "dates": "Thursday, June 17 | 7:00 pm",
        "company": "LEDA ALMAR | Artist (Argentina)",
        "title": "POSTER UNVEILING",
        "credits": "Meet and greet the Artist | Cocktail Reception",
        "synopsis": "Official unveiling of the poster artwork representing the 35th International Hispanic Theatre Festival of Miami.<br><br>www.ledaalmar.com | @leda.almar.art",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "(By invitation)"
    },
    {
        "dates": "July 8-25 | After each opening",
        "company": "BEATRIZ J. RIZK, Ph.D. | Educational Program Director",
        "title": "EDUCATIONAL COMPONENT | FORUMS",
        "credits": "Forums in Spanish and English immediately after each opening",
        "synopsis": "Educational component featuring open discussions and debate forums with directors, cast members, and theatre scholars following opening performances.",
        "venue": "Festival Venues | Miami",
        "contact": "Free admission with theater performance"
    },
    {
        "dates": "Thursday, July 8 | Before the performance",
        "company": "2021 LIFE ACHIEVEMENT IN THE PERFORMING ARTS AWARD",
        "title": "GRISELDA GAMBARO",
        "credits": "Playwright and author | Argentina",
        "synopsis": "Presentation of the 2021 Life Achievement in the Performing Arts Award to distinguished Argentine playwright and author Griselda Gambaro, a pillar of contemporary Latin American drama.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Included with performance admission"
    },
    {
        "dates": "Thursday, Friday, and Saturday; July 8, 9 and 10 | 8:30 pm<br>Sunday, July 11 | 5:00 pm",
        "company": "COMEDIA NACIONAL | Montevideo, Uruguay",
        "title": "NOCIONES BÁSICAS PARA LA CONSTRUCCIÓN DE PUENTES (Basics of Bridge Construction)",
        "credits": "Written and Directed by Jimena Márquez",
        "synopsis": "Drawing from the intimate experiences of everyone involved in the creation of this play, we have divided Mario Benedetti's story into five 'emotional zones': Montevideo, Militancy, Marketing, Exile...",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Dramatic comedy"
    },
    {
        "dates": "Friday and Saturday, July 9 and 10 | 8:30 pm<br>Sunday, July 11 | 5:00 pm",
        "company": "MURGA MADRE | Montevideo, Uruguay",
        "title": "MURGA MADRE",
        "credits": "Written by Pablo Routin | Directed by Fernando Toja | Musical Direction: Edu Lombardo",
        "synopsis": "Silences. Glances that say what is not expressed in words. Two characters lacking names, time and space... a returning through the murga. Something they were... or are. Fragments scattered to complete a story. The eternal flow of life. Yesterday, today and always... a show for the soul.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Musical theatre / Murga"
    },
    {
        "dates": "Thursday, Friday, and Saturday; July 15, 16 and 17 | 8:30 pm",
        "company": "TEATRO DE LA VUELTA | Cuenca, Ecuador",
        "title": "BARRIO CALEIDOSCOPIO (Kaleidoscope Neighborhood)",
        "credits": "Written & Directed by Carlos Gallegos",
        "synopsis": "Alfonsito wakes up with a desire to go to the store and buy a loaf of bread. To do so, he must overcome his multiple eccentric fears, appear to be like others and leave his meticulously organized, dusty home. He must walk quickly down the lonely street, avoiding teasing, sadness and any encounter with Machiavellian Magalita.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Dramatic clown"
    },
    {
        "dates": "Friday and Saturday; July 16 and 17 | 8:30 pm<br>Sunday, July 18 | 5:00 pm",
        "company": "TEATRO BOXING / EL GALPÓN | Uruguay",
        "title": "TOM PAIN (basado en nada) / TOM PAIN (based on nothing)",
        "credits": "Written by Will Eno | Directed by Lucio Hernández | Starring Rogelio Gracia (Florencio Sánchez Award)",
        "synopsis": "An apparently ordinary man turns his pain into a provocation. With honesty and humor, he shares stories from his life involving a bee sting, a boy and a dog, and a woman.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Monologue"
    },
    {
        "dates": "Saturday, July 17 | 5:00 pm",
        "company": "COLECTIVO ANIMAL (Colombia) & CONECTA MIAMI ARTS (USA)",
        "title": "UN BOSQUE ENCANTADO (An Enchanted Forest)",
        "credits": "Written & Directed by Camila Rivera, Tatiana Samper & Daniel Roa | Musical Director: Daniel Roa",
        "synopsis": "A musical and theatrical journey through the forest celebrating nature, animals and care for the planet for the whole family.<br><br>Co-presented by Key Biscayne Community Center.",
        "venue": "Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
        "contact": "Free admission & parking"
    },
    {
        "dates": "Sunday, July 18 | 2:00 - 6:00 pm",
        "company": "INTERNATIONAL CHILDREN'S DAY",
        "title": "INTERNATIONAL CHILDREN'S DAY",
        "credits": "Interactive arts workshops & performance: \"An Enchanted Forest\"",
        "synopsis": "Festive afternoon for families:<br>• 2:00 – 3:00 pm: Arts and crafts, rides, and distribution of healthy combo meals<br>• 3:00 – 4:00 pm: Workshops: Painting & Puppetry<br>• 4:00 – 5:00 pm: Workshops: Music & Dance<br>• 5:00 – 6:00 pm: Performance: \"Un bosque encantado\" (Colectivo Animal & Conecta Miami Arts)",
        "venue": "MDCA’s Mid-Stage Theatre | 2901 West Flagler Street, Miami",
        "contact": "Free admission and parking"
    },
    {
        "dates": "Thursday, Friday, and Saturday; July 22, 23, and 24 | 8:30 pm<br>Sunday, July 25 | 5:00 pm",
        "company": "TEATRO AVANTE | Miami, Florida, USA",
        "title": "UBÚ PANDEMIA (Ubu Pandemic)",
        "credits": "By Abel González Melo | Directed by Mario Ernesto Sánchez (World Premiere)",
        "synopsis": "Amid an unprecedented social crisis, King Ubú is forced to return to the island he founded: the mythical Uba, whose people have rebelled in response to widespread poverty. To top it off, a hitherto unknown pandemic is overrunning the world at lightning speed and threatens to spread into the island... (In Spanish with English supertitles)",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "World Premiere"
    },
    {
        "dates": "Friday and Saturday, July 23 and 24 | 8:30 pm<br>Sunday, July 25 | 5:00 pm",
        "company": "LOS PINCHES CHAMACOS | CDMX, Mexico",
        "title": "PAPÁ ESTÁ EN LA ATLÁNTIDA (Papa is in Atlantis)",
        "credits": "Written by Javier Malpica | Directed by Esteban Castellanos",
        "synopsis": "A touching story of orphanhood and the mutual loyalty of two brothers who set out on a journey filled with hardships to find their father in the United States.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Drama"
    }
]

# ==================== DATA EDICION 36 (2022) ====================
plays_2022_es = [
    {
        "dates": "Jueves 16 de junio | 7:00 P.M.",
        "company": "ADRIANA TORRES | Artista (México)",
        "title": "PRESENTACIÓN DEL CARTEL OFICIAL",
        "credits": "Encuentro con la Artista | Recepción y cóctel",
        "synopsis": "Presentación oficial del cartel conmemorativo de la 36ª edición del Festival Internacional de Teatro Hispano de Miami.",
        "venue": "MDCA’s Lobby | 2901 West Flagler Street, Miami",
        "contact": "(Por invitación)"
    },
    {
        "dates": "8 al 31 de julio | Después de cada estreno",
        "company": "DRA. BEATRIZ J. RIZK | Directora del Programa Educativo",
        "title": "COMPONENTE EDUCATIVO | FOROS DE DEBATE",
        "credits": "Espacio de intercambio y diálogo entre creadores y público",
        "synopsis": "Foros de análisis y debate en español e inglés inmediatamente después de cada estreno con directores, elencos e invitados especiales.",
        "venue": "Salas del Festival | Miami",
        "contact": "Entrada libre con la función"
    },
    {
        "dates": "Viernes y Sábado, 8 y 9 de julio | 8:30 P.M.<br>Domingo 10 de julio | 5:00 P.M.",
        "company": "MONTEVIDEO, URUGUAY",
        "title": "BETTE DAVIS, ¿ESTÁS AHÍ?",
        "credits": "Escrita y dirigida por Domingo Milesi",
        "synopsis": "Azucena busca el amor y el sentido de la vida tras la pérdida de su madre y su jubilación. Junto a su amiga Graciela acude a un cine de barrio que se niega a morir. Allí conocen a Aníbal, detonando un juego entre realidad y ficción donde surgen prácticas esotéricas para comunicarse con el más allá.<br><br>La obra cuenta con tecnología de sonido binaural; el público escucha la función con auriculares.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Tecnología de sonido binaural"
    },
    {
        "dates": "Jueves, Viernes y Sábado, 14, 15 y 16 de julio | 8:30 P.M.",
        "company": "MURÁTICA TEATRO | Badajoz, Extremadura, España",
        "title": "ALACRÁN O LA CEREMONIA",
        "credits": "Escrita por José Antonio Lucia | Dirigida por Román Podolsky",
        "synopsis": "Una historia de triángulo amoroso en el corazón de tabernas españolas. Emerge del esplendor gitano que desangra su historia entre palabrotas, zambra y espinas. Un canalla se reúne cada noche consigo mismo e interpreta a «La Cangrejo», el amor de su vida que ya no está, acomodándose en la tragicomedia negra y absurda de su vida.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Tragicomedia"
    },
    {
        "dates": "Viernes y Sábado, 15 y 16 de julio | 8:30 P.M.<br>Domingo 17 de julio | 5:00 P.M.",
        "company": "FUNDACIÓN FESTIVAL INTERNACIONAL TEATRO A MIL | Santiago, Chile",
        "title": "ENCUENTROS BREVES CON HOMBRES REPULSIVOS",
        "credits": "Adaptada y dirigida por Daniel Veronese",
        "synopsis": "A lo largo de ocho breves encuentros independientes, dos actores interactúan intercambiando roles. Los temas abordan la condición masculina contemporánea evidenciada ante la presencia de la mujer: en el amor, el sexo e incluso la pérdida.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Comedia dramática"
    },
    {
        "dates": "Sábado 16 de julio | 5:00 P.M.",
        "company": "SOCIETY OF THE EDUCATIONAL ARTS (Nueva York) & CONECTA MIAMI ARTS (Miami)",
        "title": "LOS COLORES DE FRIDA",
        "credits": "Escrita y dirigida por Manuel Morán",
        "synopsis": "Espectáculo bilingüe sobre la gran pintora mexicana Frida Kahlo que combina música, artes visuales, títeres y narración con participación del público. Tres Fridas en escena (la pintora, la cantante y la narradora) transportan al joven público en un viaje biográfico donde los colores sanan.",
        "venue": "Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
        "contact": "Entrada y estacionamiento gratis"
    },
    {
        "dates": "Domingo 17 de julio | 2:00 - 6:00 P.M.",
        "company": "DÍA INTERNACIONAL DEL NIÑO",
        "title": "DÍA INTERNACIONAL DEL NIÑO",
        "credits": "Talleres interactivos de arte y función teatral: «Los colores de Frida»",
        "synopsis": "Jornada gratuita infantil y familiar:<br>• 2:00 – 3:00 P.M.: Manualidades, atracciones, pintacaritas y meriendas saludables<br>• 3:00 – 4:00 P.M.: Talleres de Pintura y Títeres<br>• 4:00 – 5:00 P.M.: Talleres de Mimo<br>• 5:00 – 6:00 P.M.: Función de teatro «Los colores de Frida» (SEA & Conecta Miami Arts)",
        "venue": "MDCA’s Mid-Stage Theatre | 2901 West Flagler Street, Miami",
        "contact": "Entrada y estacionamiento gratis"
    },
    {
        "dates": "Viernes y Sábado, 22 y 23 de julio | 8:30 P.M.<br>Domingo 24 de julio | 5:00 P.M.",
        "company": "EL BALCÓN DE MEURSAULT | CABA, Argentina",
        "title": "ROTA",
        "credits": "Escrita por Natalia Villamil | Dirigida por Mariano Stolkiner",
        "synopsis": "Una madre debe reconstruir su existencia en torno a la muerte de su hijo, quien se suicidó tras cometer un femicidio. Un enfoque conmovedor donde la trama se centra en la voz de esta mujer que tuvo que criar a su hijo sola, buscando un poco de amor y comprensión.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Drama"
    },
    {
        "dates": "Viernes y Sábado, 22 y 23 de julio | 8:30 P.M.<br>Domingo 24 de julio | 5:00 P.M.",
        "company": "ENTRETENIMIENTO EDUCATIVO | San Juan, Puerto Rico",
        "title": "QUÍNTUPLES",
        "credits": "Escrita por Luis Rafael Sánchez | Dirigida por Emineh de Lourdes",
        "synopsis": "Obra cumbre de la dramaturgia puertorriqueña que retrata la realidad y contradicciones de una familia singular. Clásico nacional de alcance universal que trasciende el tiempo, siendo la obra teatral más representada en el mundo escrita por un dramaturgo puertorriqueño residente en la isla.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Comedia dramática"
    },
    {
        "dates": "Jueves 28 de julio | Antes de la función",
        "company": "PREMIO A UNA VIDA DE DEDICACIÓN A LAS ARTES ESCÉNICAS 2022",
        "title": "ADRIANA BARRAZA",
        "credits": "Actriz, directora y maestra | México",
        "synopsis": "Entrega del Premio a una Vida de Dedicación a las Artes Escénicas 2022 a la aclamada actriz y pedagoga mexicana Adriana Barraza, nominada al Premio Óscar y figura indispensable del teatro y cine internacional.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Entrada incluida con la función"
    },
    {
        "dates": "Jueves, Viernes y Sábado, 28, 29 y 30 de julio | 8:30 P.M.<br>Domingo 31 de julio | 5:00 P.M.",
        "company": "TEATRO AVANTE | Miami, EE. UU.",
        "title": "MEJOR ME CALLO",
        "credits": "Escrita por Abel González Melo | Dirigida por Mario Ernesto Sánchez",
        "synopsis": "París Cosméticos, prestigiosa empresa familiar, es líder en belleza. Pero la repentina llegada de un hábil informático, a quien el dueño otorga poderes excepcionales, desata sospechas y conflictos imprevistos que obligan a la familia a aliarse para evitar la catástrofe. (En español con supertítulos en inglés)",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Comedia dramática"
    }
]

plays_2022_en = [
    {
        "dates": "Thursday, June 16 | 7:00 pm",
        "company": "ADRIANA TORRES | Artist (Mexico)",
        "title": "INTRODUCING THE POSTER ARTIST",
        "credits": "Meet and greet the Artist | Cocktail Reception",
        "synopsis": "Official presentation of the commemorative poster artwork for the 36th International Hispanic Theatre Festival of Miami.",
        "venue": "MDCA’s Lobby | 2901 West Flagler Street, Miami",
        "contact": "(By invitation)"
    },
    {
        "dates": "July 8-31 | After each opening",
        "company": "BEATRIZ J. RIZK, Ph.D. | Educational Program Director",
        "title": "EDUCATIONAL COMPONENT | FORUMS",
        "credits": "Forums in Spanish and English immediately after each opening",
        "synopsis": "Educational component featuring open discussions and debate forums with directors, cast members, and theatre scholars following opening performances.",
        "venue": "Festival Venues | Miami",
        "contact": "Free admission with theater performance"
    },
    {
        "dates": "Friday and Saturday; July 8 and 9 | 8:30 pm<br>Sunday, July 10 | 5:00 pm",
        "company": "MONTEVIDEO, URUGUAY",
        "title": "BETTE DAVIS, ¿ESTÁS AHÍ? (Are You There, Bette Davis?)",
        "credits": "Written and Directed by Domingo Milesi",
        "synopsis": "Azucena is looking for love and the meaning of life following the loss of her mother and her retirement from work. She visits an old neighborhood movie house that refuses to die, where an encounter detonates a game between reality, fiction, and esoteric practices.<br><br>The play features binaural sound technology; the audience listens with headphones.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Binaural sound technology"
    },
    {
        "dates": "Thursday, Friday and Saturday, July 14, 15 and 16 | 8:30 pm",
        "company": "MURÁTICA TEATRO | Badajoz, Extremadura, Spain",
        "title": "ALACRÁN O LA CEREMONIA (Scorpion or The Ceremony)",
        "credits": "Written by José Antonio Lucia | Directed by Román Podolsky",
        "synopsis": "A story of a love triangle in the heart of sordid Spanish taverns. Scorpion or The Ceremony emerges from gypsy splendor amid obscenities, zambra and thorns. Alacrán comes to remember 'La Cangrejo,' the love of his life who is no longer here, settling into the black, funny, and absurd tragicomedy of his life.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Tragicomedy"
    },
    {
        "dates": "Friday and Saturday; July 15 and 16 | 8:30 pm<br>Sunday, July 17 | 5:00 pm",
        "company": "FUNDACIÓN FESTIVAL INTERNACIONAL TEATRO A MIL | Santiago, Chile",
        "title": "ENCUENTROS BREVES CON HOMBRES REPULSIVOS (Brief Encounters with Repulsive Men)",
        "credits": "Adapted & Directed by Daniel Veronese",
        "synopsis": "In the course of eight brief independent meetings, two actors interact and exchange roles back and forth, delving into the contemporary masculine condition in love, sex and even loss.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Dramatic comedy"
    },
    {
        "dates": "Saturday, July 16 | 5:00 pm",
        "company": "SOCIETY OF THE EDUCATIONAL ARTS (New York) & CONECTA MIAMI ARTS (Miami)",
        "title": "LOS COLORES DE FRIDA (Frida's Colors)",
        "credits": "Written & Directed by Manuel Morán",
        "synopsis": "A bilingual performance about the great Mexican painter Frida Kahlo combining music, visual arts, story narratives, puppets and audience participation. Three Fridas on stage transport young audiences on a biographical journey where colors heal.",
        "venue": "Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
        "contact": "Free admission and parking"
    },
    {
        "dates": "Sunday, July 17 | 2:00 - 6:00 pm",
        "company": "INTERNATIONAL CHILDREN'S DAY",
        "title": "INTERNATIONAL CHILDREN'S DAY",
        "credits": "Interactive arts workshops & performance: \"Frida's Colors\"",
        "synopsis": "Celebration for children and families:<br>• 2:00 – 3:00 pm: Arts and crafts, rides, face painting, and distribution of combo meals<br>• 3:00 – 4:00 pm: Workshops: Painting & Puppetry<br>• 4:00 – 5:00 pm: Workshops: Mime<br>• 5:00 – 6:00 pm: Performance: \"Los colores de Frida\" (SEA & Conecta Miami Arts)",
        "venue": "MDCA’s Mid-Stage Theatre | 2901 West Flagler Street, Miami",
        "contact": "Free admission and parking"
    },
    {
        "dates": "Friday and Saturday; July 22, 23 | 8:30 pm<br>Sunday, July 24 | 5:00 pm",
        "company": "EL BALCÓN DE MEURSAULT | CABA, Argentina",
        "title": "ROTA (Broken)",
        "credits": "Written by Natalia Villamil | Directed by Mariano Stolkiner",
        "synopsis": "A mother must rebuild her existence around the death of her son, who killed himself after committing femicide. The plot centers on the voice of this woman who had to raise her son on her own, searching for understanding.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Drama"
    },
    {
        "dates": "Friday and Saturday; July 22, 23 | 8:30 pm<br>Sunday, July 24 | 5:00 pm",
        "company": "ENTRETENIMIENTO EDUCATIVO | San Juan, Puerto Rico",
        "title": "QUÍNTUPLES (Quintuplets)",
        "credits": "Written by Luis Rafael Sánchez | Directed by Emineh de Lourdes",
        "synopsis": "A national Puerto Rican classic of universal scope that transcends time. Quintuplets is the most viewed theater work around the world written by a Puerto Rican playwright who resides in Puerto Rico.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Dramatic comedy"
    },
    {
        "dates": "Thursday, July 28 | Before the performance",
        "company": "2022 LIFE ACHIEVEMENT IN THE PERFORMING ARTS AWARD",
        "title": "ADRIANA BARRAZA",
        "credits": "Actress, director and educator | Mexico",
        "synopsis": "Presentation of the 2022 Life Achievement in the Performing Arts Award to Academy Award nominee and distinguished Mexican actress, director and theater educator Adriana Barraza.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Included with performance admission"
    },
    {
        "dates": "Thursday, Friday and Saturday, July 28, 29 and 30 | 8:30 pm<br>Sunday, July 31 | 5:00 pm",
        "company": "TEATRO AVANTE | Miami, U.S.A.",
        "title": "MEJOR ME CALLO (I’d Better Shut Up)",
        "credits": "Written by Abel González Melo | Directed by Mario Ernesto Sánchez",
        "synopsis": "Paris Cosmetics is the leader in beauty products. But the arrival of a clever computer wiz to whom the owner grants exceptional authority alters harmony and sparks conflicts, forcing family members to ally to avert a debacle. (In Spanish with English supertitles)",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Dramatic comedy"
    }
]

# ==================== DATA EDICION 37 (2023) ====================
plays_2023_es = [
    {
        "dates": "Jueves 22 de junio | 7:00 P.M.",
        "company": "GABRIELA ESQUIVEL | Artista (Costa Rica)",
        "title": "PRESENTACIÓN DEL CARTEL OFICIAL",
        "credits": "Encuentro con la Artista | Recepción y cóctel",
        "synopsis": "Presentación oficial de la obra artística conmemorativa de la 37ª edición del Festival Internacional de Teatro Hispano de Miami.",
        "venue": "MDCA’s Lobby | 2901 West Flagler Street, Miami",
        "contact": "(Por invitación)"
    },
    {
        "dates": "7 al 30 de julio | Después de cada estreno",
        "company": "DRA. BEATRIZ J. RIZK | Directora del Programa Educativo",
        "title": "COMPONENTE EDUCATIVO | FOROS DE DEBATE",
        "credits": "Espacio de intercambio y diálogo entre creadores y público",
        "synopsis": "Foros de análisis en español e inglés inmediatamente al término de la presentación con los elencos, directores y especialistas teatrales.",
        "venue": "Salas del Festival | Miami",
        "contact": "Entrada libre con la función"
    },
    {
        "dates": "Viernes y Sábado, 7 y 8 de julio | 8:30 P.M.<br>Domingo 9 de julio | 5:00 P.M.",
        "company": "TEATRO ESPRESSIVO | San José, Costa Rica",
        "title": "LA ISLA DE LOS HOMBRES SOLOS",
        "credits": "De José León Sánchez | Adaptación de Caridad Svich | Dirigida por José Zayas (Reposición: Humberto Canessa)",
        "synopsis": "Gran superventas literario de Costa Rica escrito por José León Sánchez en 1968. Narra los terribles sucesos en el penal de San Lucas, isla del Pacífico costarricense. Un elenco de destacados actores da vida a esta intensa reflexión sobre el valor de la libertad.",
        "venue": "MDCA's On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Drama"
    },
    {
        "dates": "Sábado y Domingo, 8 y 9 de julio | 11:00 A.M.",
        "company": "LʼAUTENTICA | Barcelona, España",
        "title": "OH, UH, AH, E! TIERRA – AIRE – FUEGO – AGUA",
        "credits": "Escrita y dirigida por Verónica Pallini",
        "synopsis": "Instalación audiovisual recomendada para niños de 1 a 5 años. Un viaje lúdico por los elementos de la naturaleza donde los pequeños son guiados por dos curiosos personajes que exploran, preguntan, se sorprenden e invitan a jugar en un espacio colmado de música, luces y sombras.",
        "venue": "Koubek Center Theatre | 2705 SW 3rd Street, Miami",
        "contact": "Entrada y valet parking gratis"
    },
    {
        "dates": "Jueves, Viernes y Sábado, 13, 14 y 15 de julio | 8:30 P.M.",
        "company": "TEJIDO ABIERTO TEATRO | Buenos Aires, Argentina",
        "title": "YO SOY DON QUIJOTE DE LA MANCHA",
        "credits": "De José Ramón Fernández | Dirigida por Jorge Eines",
        "synopsis": "Cervantes creó un caballero andante, un quijote que no ganó batallas y un loco que amaba la libertad de hacer el bien. Una búsqueda incansable de justicia y verdad donde los personajes cobran vida en un nuevo tapiz teatral lleno de ética y procedimiento.",
        "venue": "MDCA's On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Drama clásico"
    },
    {
        "dates": "Viernes y Sábado, 14 y 15 de julio | 8:30 P.M.<br>Domingo 16 de julio | 5:00 P.M.",
        "company": "COMPLEJO TEATRAL DE BUENOS AIRES | Argentina",
        "title": "CAE LA NOCHE TROPICAL",
        "credits": "De Manuel Puig | Versión teatral: Santiago Loza & Pablo Messiez | Dirigida por Pablo Messiez (Reposición: Leonor Manso)",
        "synopsis": "Basada en la novela homónima de Manuel Puig. Aborda la vejez y el afecto como necesidad para mitigar el absurdo del mundo. Dos hermanas octogenarias en Río de Janeiro conversan sobre la vida amorosa de una vecina joven, convirtiéndose en parte vital de sus vidas.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Comedia dramática"
    },
    {
        "dates": "Viernes 14 de julio | 8:30 P.M.<br>Sábado 15 de julio | 6:00 P.M.",
        "company": "PERBACCO | Buenos Aires, Argentina",
        "title": "UNA",
        "credits": "Escrita por Miriam Odorico & Giampaolo Samà | Dirigida por Giampaolo Samà",
        "synopsis": "Versión libre de «Uno, ninguno y cien mil» de Luigi Pirandello. La constatación de un detalle físico insignificante se transforma en un acontecimiento único para analizar las dudas de la existencia: ¿Quién soy? ¿Cómo nos ven los demás? Abandonar cien mil máscaras para vestir solo UNA.",
        "venue": "Koubek Center Theatre | 2705 SW 3rd Street, Miami",
        "contact": "Monólogo"
    },
    {
        "dates": "Sábado 15 de julio | 5:00 P.M.",
        "company": "LA TARTANA TEATRO | Madrid, España",
        "title": "EL GUARDIÁN DE LOS CUENTOS",
        "credits": "Escrita por Juan Muñoz e Inés Maroto | Dirigida por Juan Muñoz",
        "synopsis": "En el último día de la biblioteca, el bibliotecario abre muchos de nuestros cuentos favoritos y vive grandes aventuras. Una obra dinámica con decenas de títeres de todos los tamaños, teatro de sombras e impactante escenografía que combina lo mejor de los cuentos tradicionales.",
        "venue": "Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
        "contact": "Entrada y estacionamiento gratis"
    },
    {
        "dates": "Domingo 16 de julio | 2:00 - 6:00 P.M.",
        "company": "DÍA INTERNACIONAL DEL NIÑO",
        "title": "DÍA INTERNACIONAL DEL NIÑO",
        "credits": "Juegos de carnaval, talleres interactivos y función: «El guardián de los cuentos»",
        "synopsis": "Gran fiesta infantil y familiar:<br>• 2:00 – 3:00 P.M.: Animación y distribución de refrigerios saludables<br>• 2:30 – 5:00 P.M.: Juegos de feria y carnaval<br>• 3:00 – 5:00 P.M.: Talleres de Pintura y Títeres<br>• 5:00 – 6:00 P.M.: Función de teatro «El guardián de los cuentos» (La Tartana Teatro)",
        "venue": "MDCA’s Mid-Stage Theatre | 2901 West Flagler Street, Miami",
        "contact": "Entrada y estacionamiento gratis"
    },
    {
        "dates": "Viernes y Sábado, 21 y 22 de julio | 8:30 P.M.<br>Domingo 23 de julio | 5:00 P.M.",
        "company": "LOCO7 DANCE PUPPET THEATRE COMPANY | Nueva York, EE. UU. / Colombia",
        "title": "ALMUERZO CON SONIA",
        "credits": "Escrita y dirigida por Federico Restrepo y Denise Greber",
        "synopsis": "En agosto de 2012, agotada por una enfermedad degenerativa, Sonia Jaramillo eligió el día para morir dignamente. Durante un mes organizó almuerzos y dialogó con su familia preparándola para la despedida. Una emotiva pieza de danza y títeres que exalta la naturaleza íntima de morir.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Danza y títeres"
    },
    {
        "dates": "Viernes y Sábado, 21 y 22 de julio | 8:30 P.M.<br>Domingo 23 de julio | 5:00 P.M.",
        "company": "ARGOS TEATRO | Madrid, España",
        "title": "FORO",
        "credits": "Escrita y dirigida por Carlos Celdrán",
        "synopsis": "La visita virtual de un amigo de la infancia impulsa al protagonista a repasar el pasado y los errores de una historia compartida. Una profunda reflexión sobre la culpa, el perdón y la amistad en el contexto de una sociedad intolerante y cerrada.",
        "venue": "MDCA's On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Drama"
    },
    {
        "dates": "Viernes y Sábado, 21 y 22 de julio | 8:30 P.M.<br>Domingo 23 de julio | 5:00 P.M.",
        "company": "ESPACIO ESCÉNICA | Bogotá D.C., Colombia",
        "title": "SUPERPASITO",
        "credits": "Escrita y dirigida por Julio Escallón",
        "synopsis": "Una pareja vive en un lugar donde susurrar es la norma bajo el inminente peligro de alzar la voz. ¿Podrán convivir bajo el régimen del susurro o se atreverán a quebrar las reglas? Preguntas entre la vida y la muerte, el amor y el aburrimiento, el silencio y la voz.",
        "venue": "Koubek Center Theatre | 2705 SW 3rd Street, Miami",
        "contact": "Valet parking gratis"
    },
    {
        "dates": "Jueves 27 de julio | Antes de la función",
        "company": "PREMIO A UNA VIDA DE DEDICACIÓN A LAS ARTES ESCÉNICAS 2023",
        "title": "MIGUEL RUBIO ZAPATA",
        "credits": "Director e investigador teatral | Grupo Cultural Yuyachkani, Perú",
        "synopsis": "Entrega del Premio a una Vida de Dedicación a las Artes Escénicas 2023 al maestro Miguel Rubio Zapata, director del emblemático Grupo Cultural Yuyachkani de Perú, referente insigne del teatro ético y comunitario iberoamericano.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Entrada incluida con la función"
    },
    {
        "dates": "Jueves, Viernes y Sábado, 27, 28 y 29 de julio | 8:30 P.M.<br>Domingo 30 de julio | 5:00 P.M.",
        "company": "TEATRO AVANTE | Miami, EE. UU.",
        "title": "AL PIE DEL TÁMESIS",
        "credits": "Escrita por Mario Vargas Llosa | Dirigida por Mario Ernesto Sánchez",
        "synopsis": "Basada en personajes reales, la trama gira en torno a un imprevisto encuentro en un hotel de Londres donde los protagonistas se ven obligados a desentrañar las trampas de la memoria y desenmascarar silencios para revelar la verdad de un hecho de juventud que marcó sus vidas.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Drama"
    }
]

plays_2023_en = [
    {
        "dates": "Thursday, June 22 | 7:00 pm",
        "company": "GABRIELA ESQUIVEL | Artist (Costa Rica)",
        "title": "INTRODUCING THE POSTER ARTIST",
        "credits": "Meet and greet the Artist | Cocktail Reception",
        "synopsis": "Official presentation of the signature artwork for the 37th International Hispanic Theatre Festival of Miami.",
        "venue": "MDCA’s Lobby | 2901 West Flagler Street, Miami",
        "contact": "(By invitation)"
    },
    {
        "dates": "July 7-30 | After each opening",
        "company": "BEATRIZ J. RIZK, Ph.D. | Educational Program Director",
        "title": "EDUCATIONAL COMPONENT | FORUMS",
        "credits": "Forums in Spanish and English immediately after each presentation",
        "synopsis": "Educational component featuring open discussions and debate forums with directors, cast members, and theatre scholars following opening performances.",
        "venue": "Festival Venues | Miami",
        "contact": "Free admission with theater performance"
    },
    {
        "dates": "Friday and Saturday; July 7 & 8 | 8:30 pm<br>Sunday, July 9 | 5:00 pm",
        "company": "TEATRO ESPRESSIVO | San José, Costa Rica",
        "title": "LA ISLA DE LOS HOMBRES SOLOS (The Lonely Men´s Island)",
        "credits": "Directed by José Zayas | Revival by Humberto Canessa | Adapted by Caridad Svich",
        "synopsis": "A major Costa Rican literary bestseller written by José León Sánchez in 1968, narrating events in the San Lucas prison island. A cast of experienced actors brings this novel to life, an intense reflection on the value of freedom.",
        "venue": "MDCA's On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Drama"
    },
    {
        "dates": "Saturday and Sunday, July 8 & 9 | 11:00 am",
        "company": "LʼAUTENTICA | Barcelona, Spain",
        "title": "OH, UH, AH, E! TIERRA – AIRE – FUEGO – AGUA (Earth – Air – Fire – Water)",
        "credits": "Written & Directed by Verónica Pallini",
        "synopsis": "Audiovisual installation recommended for children 1 to 5 years of age. A ludic journey through the elements of nature guided by two curious characters who explore, ask questions, and invite the audience to play in a space filled with music, lights, and shadows.",
        "venue": "Koubek Center Theatre | 2705 SW 3rd Street, Miami",
        "contact": "Free admission and Valet parking"
    },
    {
        "dates": "Thursday, Friday and Saturday; July 13, 14 & 15 | 8:30 pm",
        "company": "TEJIDO ABIERTO TEATRO | Buenos Aires, Argentina",
        "title": "YO SOY DON QUIJOTE DE LA MANCHA (I am Don Quijote de la Mancha)",
        "credits": "By José Ramón Fernández | Directed by Jorge Eines",
        "synopsis": "Cervantes created a knight-errant who loved the freedom to do good, always searching for justice and truthfulness. The characters in this mythic novel needed a ballad showing the way to a new theatrical tapestry filled with ethics and procedure.",
        "venue": "MDCA's On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Classic drama"
    },
    {
        "dates": "Friday and Saturday; July 14, 15 | 8:30 pm<br>Sunday, July 16 | 5:00 pm",
        "company": "COMPLEJO TEATRAL DE BUENOS AIRES | Argentina",
        "title": "CAE LA NOCHE TROPICAL (Tropical Night Falling)",
        "credits": "By Manuel Puig | Stage Version: Santiago Loza & Pablo Messiez | Directed by Pablo Messiez (Revival: Leonor Manso)",
        "synopsis": "Based on Juan Manuel Puig's homonymous novel. It speaks about aging, and affection as a need in mitigating the world's absurdity. Two eighty-year-old sisters in Rio de Janeiro speak about the love life of a neighbor, an emotional show filled with delicate humor.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Dramatic comedy"
    },
    {
        "dates": "Friday; July 14 | 8:30 pm<br>Saturday, July 15 | 6:00 pm",
        "company": "PERBACCO | Buenos Aires, Argentina",
        "title": "UNA (Ones)",
        "credits": "Written by Miriam Odorico & Giampaolo Samà | Directed by Giampaolo Samà",
        "synopsis": "A free version of 'One, None and One Hundred Thousand,' a novel about personality breakdown. The corroboration of an insignificant physical detail transforms into a unique event analyzing existential doubts: Who am I? Abandoning one hundred thousand masks to wear just ONE.",
        "venue": "Koubek Center Theatre | 2705 SW 3rd Street, Miami",
        "contact": "Monologue"
    },
    {
        "dates": "Saturday, July 15 | 5:00 pm",
        "company": "LA TARTANA TEATRO | Madrid, Spain",
        "title": "EL GUARDIÁN DE LOS CUENTOS (The Tales Keeper)",
        "credits": "Written by Juan Muñoz & Inés Maroto | Directed by Juan Muñoz",
        "synopsis": "It’s the library’s last day, and the librarian opens favorite stories and embarks on adventures. Tens of puppets of all sizes, shadow theatre, and shocking sets bring five traditional tales to life.",
        "venue": "Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
        "contact": "Free admission & parking"
    },
    {
        "dates": "Sunday, July 16 | 2:00 - 6:00 pm",
        "company": "INTERNATIONAL CHILDREN'S DAY",
        "title": "INTERNATIONAL CHILDREN'S DAY",
        "credits": "Carnival games, workshops & performance: \"The Tales Keeper\"",
        "synopsis": "Festive afternoon for families:<br>• 2:00 – 3:00 pm: Entertainment and distribution of combo meals<br>• 2:30 – 5:00 pm: Carnival Games<br>• 3:00 – 5:00 pm: Workshops: Painting & Puppetry<br>• 5:00 – 6:00 pm: Performance: \"El guardián de los cuentos\" (La Tartana Teatro)",
        "venue": "MDCA’s Mid-Stage Theatre | 2901 West Flagler Street, Miami",
        "contact": "Free admission and parking"
    },
    {
        "dates": "Friday and Saturday, July 21 & 22 | 8:30 pm<br>Sunday, July 23 | 5:00 pm",
        "company": "LOCO7 DANCE PUPPET THEATRE COMPANY | New York, USA / Colombia",
        "title": "ALMUERZO CON SONIA (Lunch with Sonia)",
        "credits": "Written & Directed by Federico Restrepo & Denise Greber",
        "synopsis": "In August 2012, tired from a degenerative illness, Sonia Jaramillo chose to die with dignity. During an entire month, she organized lunches with family preparing them for her goodbye. An intimate reflection on the emotions and personal nature of dying.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Dance and puppetry"
    },
    {
        "dates": "Friday and Saturday, July 21 and 22 | 8:30 pm<br>Sunday, July 23 | 5:00 pm",
        "company": "ARGOS TEATRO | Madrid, Spain",
        "title": "FORO (Forum)",
        "credits": "Written & Directed by Carlos Celdrán",
        "synopsis": "A virtual visit from a childhood friend causes the protagonist to review the past and mistakes of their shared history. This play ponders guilt, forgiveness, and friendship against the background of an intolerant society.",
        "venue": "MDCA's On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Drama"
    },
    {
        "dates": "Friday and Saturday, July 21 and 22 | 8:30 pm<br>Sunday, July 23 | 5:00 pm",
        "company": "ESPACIO ESCÉNICA | Bogotá D.C., Colombia",
        "title": "SUPERPASITO (Careless Whispers)",
        "credits": "Written & Directed by Julio Escallón",
        "synopsis": "A couple lives in a place where whispering is the norm and raising one’s voice poses imminent danger. The couple faces questions between life and death, love and boredom, between their silence and voice.",
        "venue": "Koubek Center Theatre | 2705 SW 3rd Street, Miami",
        "contact": "Free Valet parking"
    },
    {
        "dates": "Thursday, July 27 | Before the performance",
        "company": "2023 LIFE ACHIEVEMENT IN THE PERFORMING ARTS AWARD",
        "title": "MIGUEL RUBIO ZAPATA",
        "credits": "Director and theater researcher | Grupo Cultural Yuyachkani, Peru",
        "synopsis": "Presentation of the 2023 Life Achievement in the Performing Arts Award to maestro Miguel Rubio Zapata, director of Peru's acclaimed Grupo Cultural Yuyachkani.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Included with performance admission"
    },
    {
        "dates": "Thursday, Friday and Saturday, July 27, 28 and 29 | 8:30 pm<br>Sunday, July 30 | 5:00 pm",
        "company": "TEATRO AVANTE | Miami, U.S.A.",
        "title": "AL PIE DEL TÁMESIS (On the Banks of the Thames)",
        "credits": "Written by Mario Vargas Llosa | Directed by Mario Ernesto Sánchez",
        "synopsis": "Based on real-life characters, the plot revolves around an unforeseen encounter in a London hotel where protagonists are forced to unravel traps of memory and unmask eternal silences to shed light on a youthful act that transformed their lives.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Drama"
    }
]

def generate_file(lang, year, ed_num, plays, ed_folder, out_path):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plays_html = build_plays_html(plays, ed_folder)
    page_html = get_template(lang, year, ed_num, plays_html)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page_html)
    print(f"Generated: {out_path} ({len(plays)} plays)")

# 2021 (Edición 35)
generate_file("es", "2021", 35, plays_2021_es, "Edicion_35", os.path.join(workspace, "es", "archivos-del-festival", "2021", "index.html"))
generate_file("en", "2021", 35, plays_2021_en, "Edicion_35", os.path.join(workspace, "en", "archivos-del-festival", "2021", "index.html"))

# 2022 (Edición 36)
generate_file("es", "2022", 36, plays_2022_es, "Edicion_36", os.path.join(workspace, "es", "archivos-del-festival", "2022", "index.html"))
generate_file("en", "2022", 36, plays_2022_en, "Edicion_36", os.path.join(workspace, "en", "archivos-del-festival", "2022", "index.html"))

# 2023 (Edición 37)
generate_file("es", "2023", 37, plays_2023_es, "Edicion_37", os.path.join(workspace, "es", "archivos-del-festival", "2023", "index.html"))
generate_file("en", "2023", 37, plays_2023_en, "Edicion_37", os.path.join(workspace, "en", "archivos-del-festival", "2023", "index.html"))

print("\nALL 6 PAGES GENERATED SUCCESSFULLY!")
