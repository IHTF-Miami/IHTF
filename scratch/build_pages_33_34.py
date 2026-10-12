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

# ==================== DATA EDICION 33 (2018) ====================
plays_2018_es = [
    {
        "dates": "Jueves 21 de junio | 7:00 - 11:00 P.M.",
        "company": "ANTONIO MARTORELL | Artista",
        "title": "PRESENTACIÓN DEL CARTEL OFICIAL",
        "credits": "Encuentro con el Artista | Recepción y cóctel",
        "synopsis": "Presentación oficial de la imagen representativa del 33° Festival Internacional de Teatro Hispano de Miami.<br><br>Copresentada por Miami-Dade County Auditorium | Coauspiciada por Bacardí USA.",
        "venue": "MDCA's On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "(Solo por invitación) | Estacionamiento gratis"
    },
    {
        "dates": "12 al 29 de julio | Después de cada estreno",
        "company": "DRA. BEATRIZ J. RIZK | Directora del Programa Educativo",
        "title": "COMPONENTE EDUCATIVO | FOROS DE DEBATE",
        "credits": "Espacio de intercambio y diálogo entre creadores y público",
        "synopsis": "Coloquios y foros de análisis conducidos al término de las funciones de estreno con los elencos, directores y especialistas teatrales.<br><br>En cada una de las salas participantes.",
        "venue": "Salas del Festival | Miami",
        "contact": "Entrada libre con la función"
    },
    {
        "dates": "Jueves, Viernes y Sábado, 12, 13 y 14 de julio | 8:30 P.M.<br>Domingo 15 de julio | 5:00 P.M.",
        "company": "COMPAÑÍA TOJUNTO | San Juan, Puerto Rico",
        "title": "HIJ@S DE LA BERNARDA",
        "credits": "Escrita y dirigida por Rosa Luisa Márquez | Coreografía de Jeanne D’Arc Casas",
        "synopsis": "Versión libremente adaptada de «La casa de Bernarda Alba» de Federico García Lorca. Danza-teatro expresada a través del flamenco y la danza contemporánea. Una viuda impone ocho años de luto a sus cinco hijas. En una atmósfera de autoritarismo, represión y deseo, se desencadena el drama.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Danza-teatro"
    },
    {
        "dates": "Jueves 12 de julio | 8:30 P.M. (Inmediatamente antes de la función)",
        "company": "PREMIO A UNA VIDA DE DEDICACIÓN A LAS ARTES ESCÉNICAS 2018",
        "title": "ROSA LUISA MÁRQUEZ",
        "credits": "Directora, pedagoga teatral y actriz | Puerto Rico",
        "synopsis": "Entrega del Premio a una Vida de Dedicación a las Artes Escénicas 2018 a la destacada creadora puertorriqueña Rosa Luisa Márquez en reconocimiento a su extraordinaria trayectoria y valioso aporte al teatro iberoamericano.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Entrada incluida con la función"
    },
    {
        "dates": "Viernes y Sábado, 13 y 14 de julio | 6:30 / 7:00 / 7:30 P.M.<br>Domingo 15 de julio | 3:00 / 3:30 / 4:00 P.M.",
        "company": "TEATRO AVANTE | Miami, EE. UU.",
        "title": "LA ÚLTIMA FELICIDAD",
        "credits": "Creación colectiva",
        "synopsis": "Un reencuentro reaviva viejas rencillas, secretos y deseos ocultos en una cadena de intercambios sarcásticos que oscilan entre lo absurdo y las expresiones más sentidas de una disfunción familiar, agravada por el último deseo de una mujer agonizante.",
        "venue": "MDCA’s Lobby | 2901 West Flagler Street, Miami",
        "contact": "Estacionamiento gratis"
    },
    {
        "dates": "Viernes y Sábado, 13 y 14 de julio | 8:30 P.M.<br>Domingo 15 de julio | 5:00 P.M.",
        "company": "CDN & COART+E | Madrid, España",
        "title": "#MALDITOS16",
        "credits": "Escrita por Nando López | Dirigida por Quino Falero",
        "synopsis": "A veces necesitamos volver a los lugares donde nos quebramos, caminar de regreso hacia el adolescente que fuimos y enfrentar nuestras heridas, aquellas que se abren cuando nos empeñamos en elegir quiénes queremos ser.<br><br>Coauspiciada por la Consejería Cultural de la Embajada de España.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Estacionamiento gratis"
    },
    {
        "dates": "Miércoles, Jueves y Viernes, 18, 19 y 20 de julio | 8:30 P.M.",
        "company": "ADRIANA BARRAZA VERITATEM THEATER & NOBARTE | Miami, EE. UU.",
        "title": "ÉRAMOS CUATRO",
        "credits": "Escrita y dirigida por Neher Jaqueline Briceño",
        "synopsis": "Un juego tentador diseñado para profundizar con honestidad en las relaciones matrimoniales. Dos parejas casadas, todos ellos actores, descubren accidentalmente que la profunda amistad que han compartido durante más de una década está plagada de secretos que les impiden subir juntos al escenario.",
        "venue": "Adriana Barraza Black Box | 3100 N.W. 72nd Ave. Suite 127, Miami",
        "contact": "Comedia dramática"
    },
    {
        "dates": "Jueves, Viernes y Sábado, 19, 20 y 21 de julio | 8:30 P.M.",
        "company": "TEATRO DEL ABASTO | Buenos Aires, Argentina",
        "title": "UNOS DOS",
        "credits": "Escrita y dirigida por Carolina Tejeda y José Mehrez",
        "synopsis": "Un hombre y una mujer con un pasado en común y un presente distante. Fueron amantes; ahora son recuerdos el uno para el otro. Eran dos personas que terminaron solas, aunque aún se parecen, aún piensan en común. ¿Cuánto tardarán en dejar de ser iguales?",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Estacionamiento gratis"
    },
    {
        "dates": "Viernes y Sábado, 20 y 21 de julio | 8:30 P.M.<br>Domingo 22 de julio | 5:00 P.M.",
        "company": "LA INCAPAZ | Montevideo, Uruguay",
        "title": "LA INCAPAZ",
        "credits": "De Carlos María Domínguez | Dirigida por Cecilia Baranda",
        "synopsis": "Sola y recluida, una mujer se prepara para defenderse en un juicio que resulta ser una farsa. Asaltada por la memoria y el delirio, nos cuenta su historia. La trama se sitúa en el Uruguay de finales del siglo XIX, en medio de guerras políticas y familiares.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Drama histórico"
    },
    {
        "dates": "Sábado 21 de julio | 5:00 P.M.",
        "company": "TEATRO DOBLE | Miami, EE. UU.",
        "title": "EL GATO Y LA GAVIOTA",
        "credits": "Adaptación de «Historia de una gaviota y del gato que le enseñó a volar» de Luis Sepúlveda | Escrita y dirigida por Neher Jaqueline Briceño",
        "synopsis": "La aventura de una gaviota recién nacida criada por cuatro gatos, y el compromiso del noble Zorbas de enseñarle a volar. Una tierna y conmovedora experiencia familiar que exalta la solidaridad, el amor incondicional y el cuidado del medio ambiente.<br><br>Copresentada por Key Biscayne Community Center | Coauspiciada por Key Biscayne Community Foundation, Village of Key Biscayne y Marlins Foundation.",
        "venue": "Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
        "contact": "Entrada y estacionamiento gratis"
    },
    {
        "dates": "Domingo 22 de julio | 2:00 - 6:00 P.M.",
        "company": "DÍA INTERNACIONAL DEL NIÑO | PATROCINADO POR TARGET",
        "title": "DÍA INTERNACIONAL DEL NIÑO",
        "credits": "Talleres interactivos de artes y función teatral: «El gato y la gaviota»",
        "synopsis": "Una tarde mágica y gratuita para toda la familia:<br>• 2:00 – 3:00 P.M.: Manualidades, atracciones, pintacaritas y meriendas saludables<br>• 3:00 – 4:00 P.M.: Talleres de Pintura y Títeres<br>• 4:00 – 5:00 P.M.: Talleres de Música y Percusión<br>• 5:00 – 6:00 P.M.: Función de teatro «El gato y la gaviota» (Teatro Doble)<br><br>Coauspiciado por Marlins Foundation, United Aliens Artists Foundation, Toy & Global Dreams USA, Nicklaus Children’s Hospital y Conecta: Miami Arts.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Entrada y estacionamiento gratis"
    },
    {
        "dates": "Jueves, Viernes y Sábado, 26, 27 y 28 de julio | 8:30 P.M.<br>Domingo 29 de julio | 5:00 P.M.",
        "company": "TEATRO AVANTE | Miami, Florida, EE. UU.",
        "title": "EN NINGÚN LUGAR DEL MUNDO",
        "credits": "De Abel González Melo | Dirigida por Mario Ernesto Sánchez (Estreno Mundial)",
        "synopsis": "¿Son las fronteras visibles las que definen la patria? El exilio desmiembra familias, y los años de separación producen el espejismo de un reencuentro. Porque sin amor no tendríamos patria. En ningún lugar del mundo tendríamos cabida, salvo allí donde esté el amor. (En español con supertítulos en inglés)<br><br>Coauspiciada por Miami-Dade County Department of Cultural Affairs y National Endowment for the Arts.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Estreno mundial"
    },
    {
        "dates": "Viernes y Sábado, 27 y 28 de julio | 8:30 P.M.<br>Domingo 29 de julio | 5:00 P.M.",
        "company": "LOS TRISTES TIGRES | Ciudad de México, México",
        "title": "WENSES Y LALA",
        "credits": "Escrita y dirigida por Adrián Vázquez",
        "synopsis": "Hay que buscar en nuestras raíces las fuentes del amor y de la lealtad. Una búsqueda que cobra la mayor vigencia en los tiempos que nos toca vivir. Un dueto conmovedor que nos transporta a múltiples lugares y situaciones a través del poder de la memoria.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Estacionamiento gratis"
    }
]

plays_2018_en = [
    {
        "dates": "Thursday, June 21 | 7:00 - 11:00 pm",
        "company": "ANTONIO MARTORELL | Artist",
        "title": "POSTER UNVEILING",
        "credits": "Meet and greet the Artist | Cocktail Reception",
        "synopsis": "Official presentation of the signature artwork for the 33rd International Hispanic Theatre Festival of Miami.<br><br>Co-presented by Miami-Dade County Auditorium | Co-sponsored by Bacardí USA.",
        "venue": "MDCA's On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "(By invitation only) | Free parking"
    },
    {
        "dates": "July 12-29 | After each opening",
        "company": "BEATRIZ J. RIZK, Ph.D. | Educational Program Director",
        "title": "EDUCATIONAL COMPONENT | FORUMS",
        "credits": "Forums about each opening performance",
        "synopsis": "Educational component featuring open discussions and debate forums with directors, cast members, and theatre scholars following opening performances.<br><br>At all participating venues.",
        "venue": "Festival Venues | Miami",
        "contact": "Free admission with theater performance"
    },
    {
        "dates": "Thursday, Friday, and Saturday, July 12, 13, and 14 | 8:30 pm<br>Sunday, July 15 | 5:00 pm",
        "company": "COMPAÑÍA TOJUNTO | San Juan, Puerto Rico",
        "title": "HIJ@S DE LA BERNARDA (Daughters of Bernarda)",
        "credits": "Written and directed by Rosa Luisa Márquez | Choreography by Jeanne D’Arc Casas",
        "synopsis": "Freely adapted version of Federico García Lorca's The House of Bernarda Alba. Dance-theatre rendered in flamenco and contemporary dance. A widow imposes eight years of mourning on her five daughters. In an atmosphere of authoritarianism, repression and desire, the drama unfolds.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Dance-theatre"
    },
    {
        "dates": "Thursday, July 12 | 8:30 pm (Immediately before the performance)",
        "company": "2018 LIFE ACHIEVEMENT IN THE PERFORMING ARTS AWARD",
        "title": "ROSA LUISA MÁRQUEZ",
        "credits": "Director, theater educator, and actress | Puerto Rico",
        "synopsis": "Presentation of the 2018 Life Achievement in the Performing Arts Award to outstanding Puerto Rican creator Rosa Luisa Márquez, in recognition of her extraordinary trajectory and contribution to Ibero-American theatre.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Included with performance admission"
    },
    {
        "dates": "Friday and Saturday, July 13 and 14 | 6:30 / 7:00 / 7:30 pm<br>Sunday, July 15 | 3:00 / 3:30 / 4:00 pm",
        "company": "TEATRO AVANTE | Miami, USA",
        "title": "LA ÚLTIMA FELICIDAD (The Last Happiness)",
        "credits": "A collective creation",
        "synopsis": "A meeting reignites old quarrels, secrets and hidden desires in a chain of sarcastic exchanges that move from absurd to deeply felt expressions of a family dysfunction that increases as a result of a dying woman's last wish.",
        "venue": "MDCA’s Lobby | 2901 West Flagler Street, Miami",
        "contact": "Free parking"
    },
    {
        "dates": "Friday and Saturday, July 13 and 14 | 8:30 pm<br>Sunday, July 15 | 5:00 pm",
        "company": "CDN & COART+E | Madrid, Spain",
        "title": "#MALDITOS16 / #DAMN16",
        "credits": "Written by Nando López | Directed by Quino Falero",
        "synopsis": "At times we need to return to the places where we broke down, to walk back to the adolescent we once were and face our wounds, those that open up when we are intent on choosing who we want to be.<br><br>Co-sponsored by Cultural Office of the Embassy of Spain.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Free parking"
    },
    {
        "dates": "Wednesday, Thursday and Friday, July 18, 19, and 20 | 8:30 pm",
        "company": "ADRIANA BARRAZA VERITATEM THEATER & NOBARTE | Miami, USA",
        "title": "ÉRAMOS CUATRO (We Were Four)",
        "credits": "Written & Directed by Neher Jaqueline Briceño",
        "synopsis": "A tempting game meant to delve honestly into marital relations. Two married couples, all of them actors, accidentally discover that the deep friendship they have shared for more than a decade is riddled with secrets that keep them from going onstage together.",
        "venue": "Adriana Barraza Black Box | 3100 N.W. 72nd Ave. Suite 127, Miami",
        "contact": "Dramatic comedy"
    },
    {
        "dates": "Thursday, Friday, and Saturday, July 19, 20 and 21 | 8:30 pm",
        "company": "TEATRO DEL ABASTO | Buenos Aires, Argentina",
        "title": "UNOS DOS (Two)",
        "credits": "Written & Directed by Carolina Tejeda & José Mehrez",
        "synopsis": "A man and a woman with a common past and a distant present. They were lovers; now they are memories to each other. They were two people who each ended up alone, though they still resemble each other, still think in common. How long will it take for them to stop being alike?",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Free parking"
    },
    {
        "dates": "Friday and Saturday, July 20 and 21 | 8:30 pm<br>Sunday, July 22 | 5:00 pm",
        "company": "LA INCAPAZ | Montevideo, Uruguay",
        "title": "LA INCAPAZ (Incapable)",
        "credits": "By Carlos María Domínguez | Directed by Cecilia Baranda",
        "synopsis": "Alone and confined, a woman prepares to defend herself in a trial that turns out to be a travesty. Assailed by memory and delirium, she tells us her story. The setting is Uruguay in the late 19th century, in the midst of political and family wars.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Historical drama"
    },
    {
        "dates": "Saturday, July 21 | 5:00 pm",
        "company": "TEATRO DOBLE | Miami, USA",
        "title": "EL GATO Y LA GAVIOTA (The Cat and the Seagull)",
        "credits": "Adaptation of \"Historia de una gaviota y del gato que le enseñó a volar\" by Luis Sepúlveda | Written & Directed by Neher Jaqueline Briceño",
        "synopsis": "The adventure of a baby seagull being cared for by four cats, and the commitment of one of them, the noble Zorbas, to teaching her to fly. A tender family experience addressing solidarity, unconditional love and environmental care.<br><br>Co-presented by Key Biscayne Community Center | Co-sponsored by Key Biscayne Community Foundation, Village of Key Biscayne & Marlins Foundation.",
        "venue": "Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
        "contact": "Free admission & parking"
    },
    {
        "dates": "Sunday, July 22 | 2:00 - 6:00 pm",
        "company": "INTERNATIONAL CHILDREN'S DAY | SPONSORED BY TARGET",
        "title": "INTERNATIONAL CHILDREN'S DAY",
        "credits": "Interactive arts workshops & performance: \"The Cat and the Seagull\"",
        "synopsis": "A wonderful free afternoon for children and families:<br>• 2:00 – 3:00 pm: Arts and crafts, rides, face painting and distribution of healthy combo meals<br>• 3:00 – 4:00 pm: Workshops in Painting & Puppetry<br>• 4:00 – 5:00 pm: Workshops in Music & Percussion<br>• 5:00 – 6:00 pm: Performance: \"The Cat and the Seagull\" (Teatro Doble)<br><br>Co-sponsored by Marlins Foundation, United Aliens Artists Foundation, Toy & Global Dreams USA, Nicklaus Children’s Hospital, Conecta: Miami Arts.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Free admission and parking"
    },
    {
        "dates": "Thursday, Friday, and Saturday, July 26, 27, and 28 | 8:30 pm<br>Sunday, July 29 | 5:00 pm",
        "company": "TEATRO AVANTE | Miami, Florida, USA",
        "title": "EN NINGÚN LUGAR DEL MUNDO (Nowhere in the World)",
        "credits": "By Abel González Melo | Directed by Mario Ernesto Sánchez (World Premiere)",
        "synopsis": "Do visible borders define one's homeland? Exile breaks up families, and years of separation produce the mirage of a reunion. Because without love we would have no homeland. Nowhere in the world would we belong, except there, where love is. (In Spanish with English supertitles)<br><br>Co-sponsored by Miami-Dade County Department of Cultural Affairs, National Endowment for the Arts.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "World Premiere"
    },
    {
        "dates": "Friday and Saturday, July 27 and 28 | 8:30 pm<br>Sunday, July 29 | 5:00 pm",
        "company": "LOS TRISTES TIGRES | Mexico City, Mexico",
        "title": "WENSES Y LALA (Wenses & Lala)",
        "credits": "Written & Directed by Adrián Vázquez",
        "synopsis": "We have to seek in our roots the sources of love and loyalty. A search that is most relevant in the times it is our lot to live. A duet that takes us to many places and many situations through the power of memory.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Free parking"
    }
]

# ==================== DATA EDICION 34 (2019) ====================
plays_2019_es = [
    {
        "dates": "Jueves 20 de junio | 7:00 - 10:00 P.M.",
        "company": "MANUEL TRICALLOTIS | Artista (Chile / Ecuador)",
        "title": "PRESENTACIÓN DEL CARTEL OFICIAL",
        "credits": "Encuentro con el Artista | Recepción y cóctel",
        "synopsis": "Develación oficial del afiche representativo de la 34ª edición del Festival Internacional de Teatro Hispano de Miami.<br><br>Coauspiciada por Bacardí USA.",
        "venue": "Miami-Dade County Auditorium - Lobby | 2901 West Flagler Street, Miami",
        "contact": "(Solo por invitación) | Estacionamiento gratis"
    },
    {
        "dates": "12 al 28 de julio | Después de cada estreno",
        "company": "DRA. BEATRIZ J. RIZK | Directora del Programa Educativo",
        "title": "COMPONENTE EDUCATIVO | FOROS DE DEBATE",
        "credits": "Espacio de intercambio y diálogo entre creadores y público",
        "synopsis": "Coloquios y foros de análisis conducidos al término de las funciones de estreno con los elencos, directores y especialistas teatrales.<br><br>En cada una de las salas participantes.",
        "venue": "Salas del Festival | Miami",
        "contact": "Entrada libre con la función"
    },
    {
        "dates": "Jueves, Viernes y Sábado, 11, 12 y 13 de julio | 8:30 P.M.<br>Domingo 14 de julio | 5:00 P.M.",
        "company": "NUEVE DE NUEVE | Zaragoza, España",
        "title": "LA EXTINTA POÉTICA",
        "credits": "Escrita por Eusebio Calonge | Dirigida por Paco de la Zaranda",
        "synopsis": "¿Qué hace Ofelia en nuestra era? ¿Quién escucha su lamento antes de hundirse en la vulgaridad y el tedio? Es como preguntarse por el sentido de la poesía en nuestro tiempo de velocidad y espacio.<br><br>Copresentada por Adrienne Arsht Center | Patrocinada por el Gobierno de Aragón | Coauspiciada por Centro Cultural Español, Consejería de Cultura de España, Spain Arts and Culture, y Ayuntamientos de Zaragoza y Huesca.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Drama contemporáneo"
    },
    {
        "dates": "Viernes y Sábado, 12 y 13 de julio | 8:30 P.M.<br>Domingo 14 de julio | 5:00 P.M.",
        "company": "COMPAÑÍA TEATRO IMAGEN | Santiago, Chile",
        "title": "CARTAS DE JENNY",
        "credits": "La intranscendente epopeya de Jenny Masterson | Escrita y dirigida por Gustavo Meza",
        "synopsis": "Una madre dominante, un hijo sobreprotegido y una joven que llega a romper el círculo de las certezas maternas con su encanto y desenfado.<br><br>Patrocinada por FONDART Nacional 2019, Ministerio de las Culturas, las Artes y el Patrimonio de Chile | Coauspiciada por Ministerio de Relaciones Exteriores y Consulado General de Chile en Miami.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Estacionamiento gratis"
    },
    {
        "dates": "Jueves, Viernes y Sábado, 18, 19 y 20 de julio | 8:30 P.M.",
        "company": "COMPAÑÍA DE TEATRO FUGAZ | Buenos Aires, Argentina",
        "title": "EL BULULÚ. ANTOLOGÍA ENDIABLADA",
        "credits": "Escrita y dirigida por Leticia González de Lellis y Osqui Guzmán",
        "synopsis": "El teatro es una máquina de coser que une recuerdos. Los textos del Siglo de Oro español se funden con el oro que los conquistadores se llevaron de Bolivia. Es un oro cultural que atraviesa el tiempo y que solo la memoria salva al honrar el arte de los juglares.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Estacionamiento gratis"
    },
    {
        "dates": "Viernes y Sábado, 19 y 20 de julio | 8:30 P.M.<br>Domingo 21 de julio | 5:00 P.M.",
        "company": "ALBANTA | Cádiz, España",
        "title": "BENDITA GLORIA",
        "credits": "Escrita por Juan G. Larrondo | Dirigida por Pepe Bable",
        "synopsis": "Tras la muerte de su padre, Gloria se recluye en su casa como una ermitaña en un retiro laberíntico, convirtiéndose en usurpadora, ama y esclava en una prisión que alberga a otros fantasmas con historias no menos enredadas.<br><br>Copresentada por Adrienne Arsht Center.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Tragicomedia"
    },
    {
        "dates": "Viernes 19 de julio | 8:30 P.M. (Inmediatamente antes de la función)",
        "company": "PREMIO A UNA VIDA DE DEDICACIÓN A LAS ARTES ESCÉNICAS 2019",
        "title": "PEPE BABLE",
        "credits": "Director de escena, gestor cultural y dramaturgo | España",
        "synopsis": "Entrega del Premio a una Vida de Dedicación a las Artes Escénicas 2019 al destacado director y creador español Pepe Bable, director del Festival Iberoamericano de Teatro (FIT) de Cádiz, en reconocimiento a su insigne labor en favor del teatro iberoamericano.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Entrada incluida con la función"
    },
    {
        "dates": "Sábado 20 de julio | 5:00 P.M.",
        "company": "LOS CLAVELES | Murcia, España",
        "title": "SIETE CABRITILLOS",
        "credits": "Escrita por Paca García y Aniceto Roca | Dirigida por Aniceto Roca",
        "synopsis": "Desobedeciendo a su madre, siete cabritillos dejan entrar al lobo en su casa. Pero el coraje y la astucia del más pequeño, junto con la ayuda de su madre, le darán su merecido al feroz intruso. (En español)<br><br>Copresentada por Key Biscayne Community Center | Coauspiciada por Key Biscayne Community Foundation, Village of Key Biscayne, Instituto de las Industrias Culturales y de las Artes de Murcia, United Aliens Artists Foundation, Toy y Nicklaus Children’s Hospital.",
        "venue": "Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
        "contact": "Entrada y estacionamiento gratis"
    },
    {
        "dates": "Domingo 21 de julio | 2:00 - 6:00 P.M.",
        "company": "DÍA INTERNACIONAL DEL NIÑO",
        "title": "DÍA INTERNACIONAL DEL NIÑO",
        "credits": "Talleres interactivos de arte y función teatral: «Siete cabritillos» (Los Claveles)",
        "synopsis": "Gran celebración infantil y familiar:<br>• 2:00 – 3:00 P.M.: Manualidades, atracciones, pintacaritas y meriendas saludables<br>• 3:00 – 4:00 P.M.: Talleres de Pintura y Títeres<br>• 4:00 – 5:00 P.M.: Talleres de Música y Percusión<br>• 5:00 – 6:00 P.M.: Función de teatro «Siete cabritillos» (Los Claveles, España)<br><br>Coauspiciado por el Instituto de las Industrias Culturales y de las Artes, Región de Murcia, España.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Entrada y estacionamiento gratis"
    },
    {
        "dates": "Jueves, Viernes y Sábado, 25, 26 y 27 de julio | 8:30 P.M.<br>Domingo 28 de julio | 5:00 P.M.",
        "company": "TEATRO AVANTE | Miami, Florida, EE. UU.",
        "title": "BAYAMESA",
        "credits": "De Abel González Melo | Dirigida por Mario Ernesto Sánchez (Estreno Mundial)",
        "synopsis": "Una compañía teatral tropieza con manuscritos inéditos de la poetisa María Luisa Milanés (1893-1919), ardiente feminista y patriota nacida en Bayamo, Cuba, y decide montar una obra sobre su compleja vida, descubriendo el fascinante choque con la tiranía patriarcal. (En español con supertítulos en inglés)<br><br>Copresentada por Adrienne Arsht Center | Coauspiciada por Miami-Dade County Department of Cultural Affairs, National Endowment for the Arts, Florida Division of Cultural Affairs y FAN.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Estreno mundial"
    },
    {
        "dates": "Viernes y Sábado, 26 y 27 de julio | 8:30 P.M.<br>Domingo 28 de julio | 5:00 P.M.",
        "company": "EL PRINCIPITO PRODUCCIONES | Buenos Aires, Argentina",
        "title": "MILLONES DE SEGUNDOS",
        "credits": "Escrita y dirigida por Diego Casado Rubio",
        "synopsis": "Desde los 5 años, un adolescente transexual cuenta los segundos que le quedan por vivir en un cuerpo ajeno. Tiene 554 segundos de edad y aún abriga la esperanza de comenzar su transformación. (En español con supertítulos en inglés)<br><br>Coauspiciada por Fondo Nacional de las Artes Argentina, Pro Teatro, Ministerio de Cultura de la Ciudad de Buenos Aires, Festival Internacional de Buenos Aires (FIBA) y Teatro del Abasto.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Estacionamiento gratis"
    }
]

plays_2019_en = [
    {
        "dates": "Thursday, June 20 | 7:00 - 10:00 pm",
        "company": "MANUEL TRICALLOTIS | Artist (Chile/Ecuador)",
        "title": "POSTER UNVEILING",
        "credits": "Meet and greet the Artist | Cocktail Reception",
        "synopsis": "Official presentation of the signature artwork for the 34th International Hispanic Theatre Festival of Miami.<br><br>Co-sponsored by Bacardí USA.",
        "venue": "Miami-Dade County Auditorium - Lobby | 2901 West Flagler Street, Miami",
        "contact": "(By invitation only) | Free parking"
    },
    {
        "dates": "July 12-28 | After each opening",
        "company": "BEATRIZ J. RIZK, Ph.D. | Educational Program Director",
        "title": "EDUCATIONAL COMPONENT | FORUMS",
        "credits": "Forums about each opening performance",
        "synopsis": "Educational component featuring open discussions and debate forums with directors, cast members, and theatre scholars following opening performances.<br><br>At all participating venues.",
        "venue": "Festival Venues | Miami",
        "contact": "Free admission with theater performance"
    },
    {
        "dates": "Thursday, Friday, and Saturday, July 11, 12, and 13 | 8:30 pm<br>Sunday, July 14 | 5:00 pm",
        "company": "NUEVE DE NUEVE | Zaragoza, Spain",
        "title": "LA EXTINTA POÉTICA (Extinct Poetics)",
        "credits": "Written by Eusebio Calonge | Directed by Paco de la Zaranda",
        "synopsis": "What does Ophelia do in our era? Who hears her lament before she sinks into vulgarity and tedium? It is like asking for the meaning of poetry in our age of speed and space.<br><br>Co-presented by Adrienne Arsht Center | Sponsored by the Government of Aragón, Spain | Co-sponsored by Centro Cultural Español Miami, Cultural Office of the Embassy of Spain, Spain Arts and Culture, City of Zaragoza and City of Huesca.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Contemporary drama"
    },
    {
        "dates": "Friday and Saturday, July 12 and 13 | 8:30 pm<br>Sunday, July 14 | 5:00 pm",
        "company": "COMPAÑÍA TEATRO IMAGEN | Santiago, Chile",
        "title": "CARTAS DE JENNY - La intranscendente epopeya de Jenny Masterson",
        "credits": "(Letters from Jenny - The Insignificant Epic of Jenny Masterson) | Written and directed by Gustavo Meza",
        "synopsis": "A domineering mother, an overprotected son and a girl who comes to break up the circle of maternal certainties with her charm and cheekiness.<br><br>Sponsored by FONDART Nacional 2019, Ministry of Cultures, Arts and Heritage of Chile | Co-sponsored by Ministry of Foreign Affairs and Consulate General of Chile in Miami.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Free parking"
    },
    {
        "dates": "Thursday, Friday, and Saturday, July 18, 19 and 20 | 8:30 pm",
        "company": "COMPAÑÍA DE TEATRO FUGAZ | Buenos Aires, Argentina",
        "title": "EL BULULÚ. ANTOLOGÍA ENDIABLADA (The Itinerant Actor. A Devilish Anthology)",
        "credits": "Written & Directed by Leticia González de Lellis and Osqui Guzmán",
        "synopsis": "Theatre is a sewing machine that stitches memories together. The writings from Spain’s Golden Age become fused with the gold that the conquistadors took from Bolivia. It is cultural gold that moves across time and that only memory saves by honoring the troubadour's art.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Free parking"
    },
    {
        "dates": "Friday and Saturday, July 19 and 20 | 8:30 pm<br>Sunday, July 21 | 5:00 pm",
        "company": "ALBANTA | Cádiz, Spain",
        "title": "BENDITA GLORIA (Blessed Gloria)",
        "credits": "Written by Juan G. Larrondo | Directed by Pepe Bable",
        "synopsis": "Following her father’s death, Gloria shuts herself up in her home like a hermit inside a labyrinthine retreat, becoming usurper, mistress and slave in a prison that houses other ghosts with no less tangled histories.<br><br>Co-presented by Adrienne Arsht Center.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Tragicomedy"
    },
    {
        "dates": "Friday, July 19 | 8:30 pm (Immediately before the performance)",
        "company": "2019 LIFE ACHIEVEMENT IN THE PERFORMING ARTS AWARD",
        "title": "PEPE BABLE",
        "credits": "Stage director, cultural manager, and playwright | Spain",
        "synopsis": "Presentation of the 2019 Life Achievement in the Performing Arts Award to outstanding Spanish director and cultural leader Pepe Bable, director of FIT Cádiz, in recognition of his lifetime dedication to Ibero-American theater.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "Included with performance admission"
    },
    {
        "dates": "Saturday, July 20 | 5:00 pm",
        "company": "LOS CLAVELES | Murcia, Spain",
        "title": "SIETE CABRITILLOS (Seven Little Goats)",
        "credits": "Written by Paca García and Aniceto Roca | Directed by Aniceto Roca",
        "synopsis": "Disobeying their mother, seven kids (little goats) let a wolf into their house. But their mother, and the courage and ingenuity of the youngest, deal the fierce intruder his just deserts. (In Spanish)<br><br>Co-presented by Key Biscayne Community Center | Co-sponsored by Key Biscayne Community Foundation, Village of Key Biscayne, Instituto de las Industrias Culturales y de las Artes de Murcia, United Aliens Artists Foundation, Toy, Nicklaus Children's Hospital.",
        "venue": "Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
        "contact": "Free admission & parking"
    },
    {
        "dates": "Sunday, July 21 | 2:00 - 6:00 pm",
        "company": "INTERNATIONAL CHILDREN'S DAY",
        "title": "INTERNATIONAL CHILDREN'S DAY",
        "credits": "Interactive arts workshops & performance: \"Seven Little Goats\" (Los Claveles)",
        "synopsis": "Celebration for children and families:<br>• 2:00 – 3:00 pm: Arts and crafts, rides, face painting and distribution of healthy combo meals<br>• 3:00 – 4:00 pm: Workshops in Painting & Puppetry<br>• 4:00 – 5:00 pm: Workshops in Music & Percussion<br>• 5:00 – 6:00 pm: Performance: \"Siete Cabritillos\" (Los Claveles, Spain)<br><br>Co-sponsored by Instituto de las Industrias Culturales y de las Artes, Región de Murcia, Spain.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Free admission and parking"
    },
    {
        "dates": "Thursday, Friday, and Saturday, July 25, 26, and 27 | 8:30 pm<br>Sunday, July 28 | 5:00 pm",
        "company": "TEATRO AVANTE | Miami, Florida, USA",
        "title": "BAYAMESA",
        "credits": "By Abel González Melo | Directed by Mario Ernesto Sánchez (World Premiere)",
        "synopsis": "A theatre company comes across unpublished manuscripts of the poet María Luisa Milanés (1893-1919), an ardent feminist and patriot born in Bayamo, Cuba, and undertakes to put on a play based on her complicated life, thereby discovering the fascinating story of a dangerous clash with patriarchal tyranny. (In Spanish with English supertitles)<br><br>Co-presented by Adrienne Arsht Center | Co-sponsored by Miami-Dade County Department of Cultural Affairs, National Endowment for the Arts, Florida Division of Cultural Affairs, Funding Arts Network (FAN).",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "World Premiere"
    },
    {
        "dates": "Friday and Saturday, July 26 and 27 | 8:30 pm<br>Sunday, July 28 | 5:00 pm",
        "company": "EL PRINCIPITO PRODUCCIONES | Buenos Aires, Argentina",
        "title": "MILLONES DE SEGUNDOS (Millions of Seconds)",
        "credits": "Written & Directed by Diego Casado Rubio",
        "synopsis": "Since he was 5, a transexual teen has been counting the seconds he has left to live in an alien body. He is 554 seconds old and still harbors the hope of beginning his transformation. (In Spanish with English supertitles)<br><br>Co-sponsored by Fondo Nacional de las Artes Argentina, Pro Teatro, Ministry of Culture of Buenos Aires, FIBA, Teatro del Abasto.",
        "venue": "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
        "contact": "Free parking"
    }
]

def generate_file(lang, year, ed_num, plays, ed_folder, out_path):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plays_html = build_plays_html(plays, ed_folder)
    page_html = get_template(lang, year, ed_num, plays_html)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page_html)
    print(f"Generated: {out_path} ({len(plays)} plays)")

# 2018 (Edición 33)
generate_file("es", "2018", 33, plays_2018_es, "Edicion_33", os.path.join(workspace, "es", "archivos-del-festival", "2018", "index.html"))
generate_file("en", "2018", 33, plays_2018_en, "Edicion_33", os.path.join(workspace, "en", "archivos-del-festival", "2018", "index.html"))

# 2019 (Edición 34)
generate_file("es", "2019", 34, plays_2019_es, "Edicion_34", os.path.join(workspace, "es", "archivos-del-festival", "2019", "index.html"))
generate_file("en", "2019", 34, plays_2019_en, "Edicion_34", os.path.join(workspace, "en", "archivos-del-festival", "2019", "index.html"))

print("\nALL 4 PAGES GENERATED SUCCESSFULLY!")
