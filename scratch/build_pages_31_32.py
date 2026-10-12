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
        suffix = "st" if str(ed_num).endswith("1") else "nd" if str(ed_num).endswith("2") else "th"
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

    html = f'''<!doctype html>
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
    return html

def format_play(num, ed_num, img_alt, dates, company, title, credits, synopsis, venue, contact):
    return f'''        <!-- Obra {num} -->
        <article class="play-item">
          <div class="play-top">
            <div class="play-thumb">
              <img src="../../../assets/Fotos_Archivos/Edicion_{ed_num}/cropped/Obra{num}.png" alt="{img_alt}" loading="lazy" />
            </div>
            <div class="play-meta">
              <div class="play-dates">{dates}</div>
              <div class="play-company">{company}</div>
              <h3 class="play-title">{title}</h3>
              <div class="play-credits">{credits}</div>
              <div class="play-synopsis">{synopsis}</div>
              <div class="play-venue">{venue}</div>
              <div class="play-contact">{contact}</div>
            </div>
          </div>
        </article>'''

# 2016 Plays (Edición 31)
plays_2016_es = [
    # 1
    (1, "Presentación del Cartel Oficial",
     "Jueves 16 de junio | 7:00-11:00 P.M.",
     "RICHARD BARRENECHEA | Artista",
     "PRESENTACIÓN DEL CARTEL OFICIAL",
     "Encuentro con el Artista | Recepción y cóctel con el pianista Francisco Paz",
     "Presentación oficial de la imagen representativa del 31° Festival Internacional de Teatro Hispano de Miami.<br><br>En colaboración con Miami-Dade County Auditorium | Coauspiciado por el Consulado General de Uruguay en Miami, Leon Medical Centers y Bacardí USA.",
     "Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "(Por invitación)"),
    # 2
    (2, "Exposición Fotográfica El MS St. Louis",
     "Jueves 7 a Domingo 24 de julio",
     "EXPOSICIÓN FOTOGRÁFICA",
     "EL MS ST. LOUIS",
     "Curaduría de Armando Lucas Correa | Diseño e instalación de Ernesto Padilla",
     "Exposición documental y fotográfica que rememora el trágico viaje de 1939 de los refugiados judíos a bordo del buque transatlántico MS St. Louis.<br><br>Copresentada por Adrienne Arsht Center | Coauspiciada por Funding Arts Network (FAN) y Leon Medical Centers.",
     "Carnival Studio Theater Lobby, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "Entrada libre con las funciones del teatro"),
    # 3
    (3, "No daré hijos, daré versos",
     "Jueves, Viernes y Sábado, 7, 8 y 9 de julio | 8:30 P.M.<br>Domingo 10 de julio | 5:00 P.M.",
     "TEATRO LA MORENA | Montevideo, Uruguay",
     "NO DARÉ HIJOS, DARÉ VERSOS (I Won’t Bring Forth Children But Poems)",
     "Escrita y dirigida por Marianella Morena",
     "Una obra apasionada e incisiva sobre la poeta Delmira Agustini, pionera de la literatura erótica femenina hispanoamericana. Una indagación sobre el amor, la libertad, el deseo y la violencia contra la mujer a través de una dramaturgia contemporánea y vibrante. (En español)<br><br>Coauspiciada por el Consulado General de Uruguay en Miami.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Entradas:</strong> 305.949.6722 | 866.949.6722 | www.arshtcenter.org"),
    # 4
    (4, "Premio a una Vida de Dedicación Nidia Telles",
     "Jueves 7 de julio | Al finalizar la función inaugural",
     "URUGUAY",
     "PREMIO A UNA VIDA DE DEDICACIÓN A LAS ARTES ESCÉNICAS 2016",
     "Homenaje a Nidia Telles",
     "Reconocimiento a la destacada trayectoria de la primera actriz uruguaya Nidia Telles por su invaluable contribución al teatro hispanoamericano.<br><br>Coauspiciado por el Consulado General de Uruguay en Miami.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "Ceremonia especial"),
    # 5
    (5, "Cacería",
     "Viernes y Sábado, 8 y 9 de julio | 8:30 P.M.<br>Domingo 10 de julio | 5:00 P.M.",
     "TEATRO PROMETEO | Miami, Florida, EE. UU.",
     "CACERÍA (The Hunt)",
     "Adaptación libre de Las brujas de Salem de Arthur Miller por Cristina Rebull e Iliana Prieto | Dirigida por Joann Yarrow y Cristina Rebull",
     "Una revisión vibrante y contemporánea del clásico de Miller sobre el fanatismo, la intolerancia y la caza de brujas, donde las acusaciones infundadas y el miedo colectivo desatan la histeria en una comunidad implacable. (En español con supertítulos en inglés)",
     "Koubek Theatre, Miami Dade College | 2705 SW 3rd Street, Miami",
     "<strong>Entradas:</strong> 305.237.3262 | www.teatroprometeo.org | www.brownpapertickets.com"),
    # 6
    (6, "Del manantial del corazón",
     "Viernes y Sábado, 8 y 9 de julio | 8:30 P.M.<br>Domingo 10 de julio | 5:00 P.M.",
     "SA’AS TUN | Yucatán, México",
     "DEL MANANTIAL DEL CORAZÓN (From the Wellspring of the Heart)",
     "Escrita y dirigida por Conchi León",
     "Una experiencia íntima y mística inspirada en las tradiciones, mitos y ritos mayas alrededor del nacimiento y la maternidad, guiada por testimonios conmovedores de mujeres indígenas. (En español)<br><br>Auspiciada por Miami-Dade County Auditorium.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Entradas:</strong> 305.547.5414 | 800.745.3000 | www.miamidadecountyauditorium.org"),
    # 7
    (7, "Los espejos de Don Quijote",
     "Viernes y Sábado, 15 y 16 de julio | 8:30 P.M.<br>Domingo 17 de julio | 5:00 P.M.",
     "PÁNICOESCÉNICO PRODUCCIONES | Madrid, España",
     "LOS ESPEJOS DE DON QUIJOTE (Mirrors of Don Quixote)",
     "Escrita y dirigida por Alberto Herreros Salcedo",
     "Un encuentro ficticio en prisión entre Miguel de Cervantes y William Shakespeare en el que intercambian vivencias, pasiones y reflexiones sobre la locura, la genialidad y la inmortalidad de sus creaciones.<br><br>Coauspiciada por Fundación Contamos Contigo y la Comisión del IV Centenario de la Muerte de Cervantes.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Entradas:</strong> 305.949.6722 | 866.949.6722 | www.arshtcenter.org"),
    # 8
    (8, "La isla desierta",
     "Jueves, Viernes y Sábado, 14, 15 y 16 de julio | 8:30 P.M.",
     "GRUPO OJCURO | Buenos Aires, Argentina",
     "LA ISLA DESIERTA (The Desert Island)",
     "Escrita por Roberto Arlt y José Menchaca | Dirigida por José Menchaca",
     "En una gris oficina portuaria, unos oficinistas atrapados en la monotonía y la rutina sueñan con escapar hacia islas paradisíacas. Una obra teatral representada en completa oscuridad utilizando estímulos sonoros, táctiles y olfativos.<br><br>Auspiciada por Miami-Dade County Auditorium | Coauspiciada por Teatro Ciego de Argentina.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Entradas:</strong> 305.547.5414 | 800.745.3000 | www.miamidadecountyauditorium.org"),
    # 9
    (9, "Piedra a piedra",
     "Sábado 16 de julio | 5:00 P.M.",
     "EL TEATRE DE L’HOME DIBUIXAT | Valencia, España",
     "PIEDRA A PIEDRA (Stone by Stone)",
     "Escrita y dirigida por Rosa Díaz",
     "Un hombre solitario pasea por la playa y descubre que las piedras pueden cobrar vida, transformándose en personajes llenos de poesía y ternura. Al terminar la función, los niños interactúan con el actor y disfrutan de una presentación de Short Chef sobre nutrición infantil.<br><br>En colaboración con Key Biscayne Community Center | Coauspiciada por Centro Cultural Español de Miami, INAEM y Marlins Foundation.",
     "Island Room, Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
     "Entrada y estacionamiento gratis | <strong>Reservaciones:</strong> 305.365.8900"),
    # 10
    (10, "Día Internacional del Niño — Piedra a piedra",
     "Domingo 17 de julio | 2:00-7:00 P.M.",
     "EL TEATRE DE L’HOME DIBUIXAT | Valencia, España",
     "DÍA INTERNACIONAL DEL NIÑO — PIEDRA A PIEDRA",
     "Escrita y dirigida por Rosa Díaz",
     "<strong>2:00-3:00 P.M.</strong> | Manualidades, atracciones, pintacaritas y distribución de meriendas<br><strong>3:00-4:30 P.M.</strong> | Talleres interactivos: actuación, danza, voz/música, pintura y títeres<br><strong>4:45-5:45 P.M.</strong> | Presentación de los niños de los talleres<br><strong>6:00-7:00 P.M.</strong> | FUNCIÓN: <em>Piedra a piedra</em>.<br><br>Auspiciado por TARGET, Miami-Dade County Auditorium, Centro Cultural Español de Miami, INAEM y Marlins Foundation.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "Entrada y estacionamiento gratis | <strong>Información:</strong> 305.547.5414"),
    # 11
    (11, "Conferencia Educativa",
     "Viernes 22 de julio | 2:00-5:00 P.M.",
     "DRA. BEATRIZ J. RIZK | Directora del Programa Educativo",
     "CONFERENCIA EDUCATIVA | TENDENCIAS EN LAS ARTES ESCÉNICAS",
     "Conmemorando el Trágico Viaje de 1939 del MS St. Louis",
     "Conferencia magistral y panel de discusión sobre las tendencias contemporáneas del teatro hispano y latinoamericano, centrada en la memoria histórica del MS St. Louis y su resonancia artística actual. (En español e inglés)<br><br>En colaboración con Teatro Prometeo, Miami Dade College, Wolfson Campus.",
     "Miami Dade College, Wolfson Campus, Edificio 2, Salón 2106 | 300 NE 2nd Avenue, Miami",
     "Entrada y estacionamiento gratis | <strong>Información:</strong> 305.445.8877"),
    # 12
    (12, "El puerto de los cristales rotos",
     "Jueves, Viernes y Sábado, 21, 22 y 23 de julio | 8:30 P.M.<br>Domingo 24 de julio | 5:00 P.M.",
     "TEATRO AVANTE | Miami, Florida, EE. UU. (Estreno Mundial)",
     "EL PUERTO DE LOS CRISTALES ROTOS (Harbor of Broken Glass)",
     "Escrita por Mario Ernesto Sánchez y Patricia Suárez | Dirigida por Mario Ernesto Sánchez",
     "El drama de los refugiados judíos que a bordo del buque MS St. Louis zarparon de Alemania en 1939 buscando asilo en La Habana y Miami, y a quienes se les negó la entrada, viéndose forzados a retornar al horror nazi. Una tragedia histórica que interpela el presente sobre la intolerancia y el refugio humano. (En español con supertítulos en inglés)<br><br>Coauspiciada por Miami-Dade County Department of Cultural Affairs, National Endowment for the Arts y State of Florida Division of Cultural Affairs.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Entradas:</strong> 305.949.6722 | 866.949.6722 | www.arshtcenter.org"),
    # 13
    (13, "El sistema solar",
     "Viernes y Sábado, 22 y 23 de julio | 8:30 P.M.<br>Domingo 24 de julio | 5:00 P.M.",
     "EL SISTEMA SOLAR | Lima, Perú",
     "EL SISTEMA SOLAR (The Solar System)",
     "Escrita y dirigida por Mariana de Althaus",
     "Durante una tensa cena de Nochebuena en Lima, una familia disfuncional confronta secretos, reproches y heridas no cicatrizadas cuando el padre anciano presenta a su nueva pareja, la exnovia de su propio hijo. Un retrato desgarrador y a la vez tierno de los vínculos familiares. (En español)<br><br>Auspiciada por Miami-Dade County Auditorium | Coauspiciada por Costamar Travel.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Entradas:</strong> 305.547.5414 | 800.745.3000 | www.miamidadecountyauditorium.org")
]

plays_2016_en = [
    # 1
    (1, "Official Poster Unveiling",
     "Thursday, June 16 | 7:00-11:00pm",
     "RICHARD BARRENECHEA | Artist",
     "OFFICIAL POSTER UNVEILING",
     "Meet and greet the Artist | Cocktail Reception, featuring pianist Francisco Paz",
     "Official presentation of the signature artwork for the 31st International Hispanic Theatre Festival of Miami.<br><br>In collaboration with Miami-Dade County Auditorium | Co-sponsored by the Consulate General of Uruguay in Miami, Leon Medical Centers, and Bacardí USA.",
     "Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "(By invitation)"),
    # 2
    (2, "Photography Exhibit The MS St. Louis",
     "Thursday, July 7, through Sunday, July 24",
     "PHOTOGRAPHY EXHIBIT",
     "THE MS ST. LOUIS",
     "Curated by Armando Lucas Correa | Design and Installation by Ernesto Padilla",
     "A documentary and photographic exhibition commemorating the tragic 1939 journey of the Jewish refugees aboard the transatlantic liner MS St. Louis.<br><br>Co-presented by the Adrienne Arsht Center | Co-sponsored by Funding Arts Network (FAN) and Leon Medical Centers.",
     "Carnival Studio Theater Lobby, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "Free admission during theater performances"),
    # 3
    (3, "I Won’t Bring Forth Children But Poems",
     "Thursday, Friday, and Saturday; July 7, 8, and 9 | 8:30pm<br>Sunday, July 10 | 5:00pm",
     "TEATRO LA MORENA | Montevideo, Uruguay",
     "NO DARÉ HIJOS, DARÉ VERSOS (I Won’t Bring Forth Children But Poems)",
     "Written and directed by Marianella Morena",
     "A passionate and incisive play about the poet Delmira Agustini, a pioneer of female erotic literature in Latin America. An inquiry into love, freedom, desire, and violence against women through contemporary, vibrant dramaturgy. (In Spanish)<br><br>Co-sponsored by the Consulate General of Uruguay in Miami.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Tickets:</strong> 305.949.6722 | 866.949.6722 (toll free) | www.arshtcenter.org"),
    # 4
    (4, "2016 Life Achievement Award Nidia Telles",
     "Thursday, July 7 | Immediately following the performance",
     "URUGUAY",
     "2016 LIFE ACHIEVEMENT IN THE PERFORMING ARTS AWARD",
     "Honoring Nidia Telles",
     "Recognition of the distinguished career of veteran Uruguayan actress Nidia Telles for her invaluable contribution to Hispanic American theater.<br><br>Co-sponsored by the Consulate General of Uruguay in Miami.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "Special ceremony"),
    # 5
    (5, "The Hunt",
     "Friday and Saturday, July 8 and 9 | 8:30pm<br>Sunday, July 10 | 5:00pm",
     "TEATRO PROMETEO | Miami, Florida, USA",
     "CACERÍA (The Hunt)",
     "Freely adapted from Arthur Miller's The Crucible by Cristina Rebull and Iliana Prieto | Directed by Joann Yarrow and Cristina Rebull",
     "A vibrant, contemporary reimagining of Miller's classic on fanaticism, intolerance, and witch-hunts, where groundless accusations and collective fear unleash hysteria upon a ruthless community. (In Spanish with English supertitles)",
     "Koubek Theatre, Miami Dade College | 2705 SW 3rd Street, Miami",
     "<strong>Tickets:</strong> 305.237.3262 | www.teatroprometeo.org | www.brownpapertickets.com"),
    # 6
    (6, "From the Wellspring of the Heart",
     "Friday and Saturday, July 8 and 9 | 8:30pm<br>Sunday, July 10 | 5:00pm",
     "SA’AS TUN | Yucatan, Mexico",
     "DEL MANANTIAL DEL CORAZÓN (From the Wellspring of the Heart)",
     "Written and directed by Conchi León",
     "An intimate and mystical experience inspired by Mayan traditions, myths, and rituals surrounding childbirth and motherhood, guided by the poignant testimonies of indigenous women. (In Spanish)<br><br>Sponsored by Miami-Dade County Auditorium.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Tickets:</strong> 305.547.5414 | 800.745.3000 (toll free) | www.miamidadecountyauditorium.org"),
    # 7
    (7, "Mirrors of Don Quixote",
     "Friday and Saturday, July 15 and 16 | 8:30pm<br>Sunday, July 17 | 5:00pm",
     "PÁNICOESCÉNICO PRODUCCIONES | Madrid, Spain",
     "LOS ESPEJOS DE DON QUIJOTE (Mirrors of Don Quixote)",
     "Written and directed by Alberto Herreros Salcedo",
     "A fictional prison encounter between Miguel de Cervantes and William Shakespeare where they exchange experiences, passions, and reflections on madness, genius, and the immortality of their creations.<br><br>Co-sponsored by Fundación Contamos Contigo and IV Centenario de la Muerte de Cervantes.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Tickets:</strong> 305.949.6722 | 866.949.6722 (toll free) | www.arshtcenter.org"),
    # 8
    (8, "The Desert Island",
     "Thursday, Friday, and Saturday; July 14, 15, and 16 | 8:30pm",
     "GRUPO OJCURO | Buenos Aires, Argentina",
     "LA ISLA DESIERTA (The Desert Island)",
     "Written by Roberto Arlt and José Menchaca | Directed by José Menchaca",
     "In a drab port office, clerks trapped in routine and monotony dream of escaping to paradisiacal islands. Performed in complete darkness using auditory, tactile, and olfactory stimuli.<br><br>Sponsored by Miami-Dade County Auditorium | Co-sponsored by Teatro Ciego de Argentina.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Tickets:</strong> 305.547.5414 | 800.745.3000 (toll free) | www.miamidadecountyauditorium.org"),
    # 9
    (9, "Stone by Stone",
     "Saturday, July 16 | 5:00pm",
     "EL TEATRE DE L’HOME DIBUIXAT | Valencia, Spain",
     "PIEDRA A PIEDRA (Stone by Stone)",
     "Written and directed by Rosa Díaz",
     "A solitary man walks along the beach and discovers that stones can come to life, becoming characters full of poetry and tenderness. Following the performance, children interact with the actor followed by a presentation by Short Chef on nutrition.<br><br>In collaboration with Key Biscayne Community Center | Co-sponsored by Centro Cultural Español de Miami, INAEM, and the Marlins Foundation.",
     "Island Room, Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
     "Free admission and parking | <strong>Reservations:</strong> 305.365.8900"),
    # 10
    (10, "International Children's Day — Stone by Stone",
     "Sunday, July 17 | 2:00-7:00pm",
     "EL TEATRE DE L’HOME DIBUIXAT | Valencia, Spain",
     "INTERNATIONAL CHILDREN'S DAY — STONE BY STONE",
     "Written and directed by Rosa Díaz",
     "<strong>2:00-3:00pm</strong> | Arts and crafts, rides, face painting, and distribution of combo meals<br><strong>3:00-4:30pm</strong> | Interactive workshops: acting, dance, voice/music, painting, and puppetry<br><strong>4:45-5:45pm</strong> | Workshop participants' presentation<br><strong>6:00-7:00pm</strong> | PERFORMANCE: <em>Stone by Stone</em>.<br><br>Sponsored by TARGET, Miami-Dade County Auditorium, Centro Cultural Español de Miami, INAEM, and the Marlins Foundation.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "Free admission and parking | <strong>Information:</strong> 305.547.5414"),
    # 11
    (11, "Educational Conference",
     "Friday, July 22 | 2:00-5:00pm",
     "BEATRIZ J. RIZK, Ph.D. | Educational Program Director",
     "EDUCATIONAL CONFERENCE | TRENDS IN LATINO PERFORMING ARTS",
     "Commemorating the Tragic 1939 Voyage of the MS St. Louis",
     "Keynote address and panel discussion examining current trends in Hispanic and Latin American theater, focusing on the historical memory of the MS St. Louis and its artistic resonance today. (In Spanish and English)<br><br>In collaboration with Teatro Prometeo, Miami Dade College, Wolfson Campus.",
     "Miami Dade College, Wolfson Campus, Building 2, Room 2106 | 300 NE 2nd Avenue, Miami",
     "Free admission and parking | <strong>Information:</strong> 305.445.8877"),
    # 12
    (12, "Harbor of Broken Glass",
     "Thursday, Friday, and Saturday; July 21, 22, and 23 | 8:30pm<br>Sunday, July 24 | 5:00pm",
     "TEATRO AVANTE | Miami, Florida, USA (World Premiere)",
     "EL PUERTO DE LOS CRISTALES ROTOS (Harbor of Broken Glass)",
     "Written by Mario Ernesto Sánchez and Patricia Suárez | Directed by Mario Ernesto Sánchez",
     "The tragedy of the Jewish refugees aboard the MS St. Louis who sailed from Germany in 1939 seeking asylum in Havana and Miami, only to be denied entry and forced back to the Nazi horrors. A historical tragedy confronting the present on intolerance and human refuge. (In Spanish with English supertitles)<br><br>Co-sponsored by Miami-Dade County Department of Cultural Affairs, National Endowment for the Arts, and State of Florida Division of Cultural Affairs.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Tickets:</strong> 305.949.6722 | 866.949.6722 (toll free) | www.arshtcenter.org"),
    # 13
    (13, "The Solar System",
     "Friday and Saturday, July 22 and 23 | 8:30pm<br>Sunday, July 24 | 5:00pm",
     "EL SISTEMA SOLAR | Lima, Peru",
     "EL SISTEMA SOLAR (The Solar System)",
     "Written and directed by Mariana de Althaus",
     "During a tense Christmas Eve dinner in Lima, a dysfunctional family confronts buried secrets, reproaches, and unhealed wounds when the elderly father introduces his new partner—his own son's ex-girlfriend. A poignant yet tender portrait of family dynamics. (In Spanish)<br><br>Sponsored by Miami-Dade County Auditorium | Co-sponsored by Costamar Travel.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Tickets:</strong> 305.547.5414 | 800.745.3000 (toll free) | www.miamidadecountyauditorium.org")
]

# 2017 Plays (Edición 32)
plays_2017_es = [
    # 1
    (1, "Presentación del Cartel Oficial",
     "Jueves 15 de junio | 7:00-10:00 P.M.",
     "TONY CARBONELL | Artista",
     "PRESENTACIÓN DEL CARTEL OFICIAL",
     "Encuentro con el Artista | Recepción y cóctel",
     "Develación oficial del afiche representativo de la 32ª edición del Festival Internacional de Teatro Hispano de Miami.<br><br>Copresentada por MIAMI-DADE COUNTY AUDITORIUM | Coauspiciada por BACARDÍ USA.",
     "MDCA's On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
     "(Solo por invitación)"),
    # 2
    (2, "Componente Educativo",
     "6 al 23 de julio | Después de cada estreno",
     "DRA. BEATRIZ J. RIZK | Directora del Programa Educativo",
     "COMPONENTE EDUCATIVO | FOROS DE DEBATE",
     "Espacio de intercambio y diálogo entre creadores y público",
     "Coloquios y foros de análisis conducidos al término de las funciones de estreno con los elencos, directores y especialistas teatrales.<br><br>En cada una de las salas participantes.",
     "Salas del Festival | Miami",
     "Entrada libre con la función"),
    # 3
    (3, "Premio a una Vida de Dedicación Julieta Egurrola",
     "Jueves 6 de julio | 8:30 P.M. (Inmediatamente antes de la función inaugural)",
     "MÉXICO",
     "PREMIO A UNA VIDA DE DEDICACIÓN A LAS ARTES ESCÉNICAS 2017",
     "Homenaje a Julieta Egurrola",
     "Distinción a la eminente actriz mexicana Julieta Egurrola por su fecunda y ejemplar trayectoria en las tablas, el cine y la televisión.<br><br>Copresentado por el INSTITUTO CULTURAL DE MÉXICO EN MIAMI y AEROMÉXICO.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "Ceremonia de entrega"),
    # 4
    (4, "Algo de un tal Shakespeare",
     "Jueves, Viernes y Sábado, 6, 7 y 8 de julio | 8:30 P.M.<br>Domingo 9 de julio | 5:00 P.M.",
     "LOS TRISTES TIGRES | Ciudad de México, México",
     "ALGO DE UN TAL SHAKESPEARE (Something by One Shakespeare)",
     "Escrita y dirigida por Adrián Vázquez",
     "Una invitación a jugar en el escenario y a ser irreverentes. Entretenimiento compuesto de improvisaciones y giros lúdicos sobre las obras de William Shakespeare, acercando el teatro isabelino a jóvenes y adultos de manera divertida y vital. (En español)<br><br>Coauspiciada por Fondo Nacional para la Cultura y las Artes (FONCA) de México.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Entradas:</strong> 305.949.6722 | 866.949.6722 | www.arshtcenter.org"),
    # 5
    (5, "Todo lo que está a mi lado",
     "Viernes y Sábado, 7 y 8 de julio | 6:00-8:30 P.M.<br>Domingo 9 de julio | 3:00-4:30 P.M.",
     "FERNANDO RUBIO | Buenos Aires, Argentina",
     "TODO LO QUE ESTÁ A MI LADO (Everything That’s By My Side)",
     "Escrita y dirigida por Fernando Rubio",
     "Una experiencia teatral íntima e inmersiva. En camas individuales instaladas en el vestíbulo, una actriz y un solo espectador comparten una historia susurrada, explorando la intimidad, la memoria infantil, los lazos humanos y el tiempo. (En español)<br><br>Coauspiciada por Miami-Dade County Auditorium.",
     "Miami-Dade County Auditorium Lobby | 2901 West Flagler Street, Miami",
     "<strong>Entradas:</strong> 305.547.5414 | www.miamidadecountyauditorium.org"),
    # 6
    (6, "Piedras preciosas",
     "Viernes y Sábado, 7 y 8 de julio | 8:30 P.M.<br>Domingo 9 de julio | 5:00 P.M.",
     "AL FIN Y AL CABO | Marbella, España",
     "PIEDRAS PRECIOSAS (Precious Stones)",
     "Escrita por Pablo Díaz | Dirigida por Andrea Chacón Álvarez y Raúl Mancilla",
     "En los años sesenta, el artista Jean Cocteau pasó largas temporadas en Marbella disfrutando de su vida social. La obra recrea la relación fascinante entre Cocteau y un joven bailaor flamenco, mostrando su mutuo aprendizaje y afecto. (En español)<br><br>Coauspiciada por Otoclinic, Teloneras, Ayto. Marbella, Centro Cultural Español de Miami (CCEMiami) y Miami-Dade County Auditorium.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Entradas:</strong> 305.547.5414 | 800.745.3000 | www.miamidadecountyauditorium.org"),
    # 7
    (7, "Édipo",
     "Jueves, Viernes y Sábado, 13, 14 y 15 de julio | 8:30 P.M.",
     "MÁRMORE - COMPANHIA DO CHAPITÔ | Lisboa, Portugal",
     "ÉDIPO (Oedipus)",
     "Creación colectiva sobre el clásico de Sófocles | Dirigida por José Carlos García",
     "Edipo huye de su inexorable destino de parricidio e incesto, resolviendo enigmas y tropezando con el destino. Una comedia física y visual vertiginosa que cuenta la tragedia clásica griega de la manera más delirante y desternillante. (En español con supertítulos en inglés)<br><br>Coauspiciada por Miami-Dade County Auditorium.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Entradas:</strong> 305.547.5414 | 800.745.3000 | www.miamidadecountyauditorium.org"),
    # 8
    (8, "Los monstruos",
     "Viernes y Sábado, 14 y 15 de julio | 8:30 P.M.<br>Domingo 16 de julio | 5:00 P.M.",
     "COMPAÑÍA CRIOLLA | Buenos Aires, Argentina",
     "LOS MONSTRUOS (The Monsters)",
     "Escrita y dirigida por Emiliano Dionisi",
     "Claudio y Sandra saben que sus hijos son especiales y únicos. Es verdad que tienen problemas de conducta y rara vez los invitan a cumpleaños, pero solo un buen padre puede protegerlos de un mundo monstruoso. Un musical de culto aclamado internacionalmente. (En español)<br><br>Coauspiciada por Ministerio de Cultura del Gobierno de la Ciudad de Buenos Aires y Consulado General de Argentina en Miami.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Entradas:</strong> 305.949.6722 | 866.949.6722 | www.arshtcenter.org"),
    # 9
    (9, "Nidos",
     "Sábado 15 de julio | 5:00 P.M.",
     "TELONCILLO TEATRO | Valladolid, España",
     "NIDOS (Nests)",
     "Escrita y dirigida por Ana Gallego y Ángel Sánchez",
     "Un espectáculo poético de música en directo, sonidos, formas y colores inspirado en el universo de los pájaros y sus nidos, especialmente pensado para la primera infancia y sus familias. (En español)<br><br>Copresentado por Key Biscayne Community Center | Coauspiciado por TARGET, INAEM de España, Key Biscayne Community Foundation, Village of Key Biscayne y Marlins Foundation.",
     "Island Room, Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
     "Entrada y estacionamiento gratis | <strong>Reservaciones:</strong> 305.365.8900"),
    # 10
    (10, "Día Internacional del Niño — Nidos",
     "Domingo 16 de julio | 2:00-7:00 P.M.",
     "TELONCILLO TEATRO | Valladolid, España",
     "DÍA INTERNACIONAL DEL NIÑO — NIDOS",
     "Escrita y dirigida por Ana Gallego y Ángel Sánchez",
     "<strong>2:00-3:00 P.M.</strong> | Manualidades, atracciones, pintacaritas y distribución de meriendas<br><strong>3:00-4:30 P.M.</strong> | Talleres interactivos: actuación, danza, voz/música, pintura y títeres<br><strong>4:30-5:30 P.M.</strong> | Presentación de los niños de los talleres<br><strong>6:00-7:00 P.M.</strong> | FUNCIÓN: <em>Nidos</em> por Teloncillo Teatro y animación gastronómica infantil con Short Chef.<br><br>Coauspiciado por TARGET, Centro Cultural Español (CCEMiami), Junta de Castilla y León, Teatro Calderón, Ministerio de Cultura de España, INAEM, Te Veo, Artesa, Marlins Foundation y United Aliens Artists.",
     "MDCA's On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
     "Entrada y estacionamiento gratis | <strong>Información:</strong> 305.547.5414"),
    # 11
    (11, "Notas que saben a olvido",
     "Jueves, Viernes y Sábado, 20, 21 y 22 de julio | 8:30 P.M.<br>Domingo 23 de julio | 5:00 P.M.",
     "TEATRO AVANTE | Miami, Florida, EE. UU. (Estreno en EE. UU.)",
     "NOTAS QUE SABEN A OLVIDO (Forgetting)",
     "Escrita por Araceli Mariel Arreche | Dirigida por Mario Ernesto Sánchez",
     "Utilizando el poder comunicativo del teatro para explorar el síndrome de Alzheimer, la obra aborda la compleja situación de quienes conviven con este padecimiento cognitivo, reflexionando sobre el afecto, la memoria y la relación entre el paciente y su entorno familiar. (En español con supertítulos en inglés)<br><br>Coauspiciada por Miami-Dade County Department of Cultural Affairs, National Endowment for the Arts y State of Florida Division of Cultural Affairs.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Entradas:</strong> 305.949.6722 | 866.949.6722 | www.arshtcenter.org"),
    # 12
    (12, "Tres viejos mares",
     "Viernes y Sábado, 21 y 22 de julio | 8:30 P.M.<br>Domingo 23 de julio | 5:00 P.M.",
     "ESCENA NORTE (El Salvador) / RAYUELA TEATRO (Guatemala) / GRUPO TEATRAL BAMBÚ (Honduras)",
     "TRES VIEJOS MARES (Three Old Seas)",
     "Escrita por Arístides Vargas | Dirigida por Arístides Vargas y Charo Francés",
     "Tres ancianos se encuentran frente al mar para hablar del ocaso de sus vidas. En sus encuentros hay rivalidad, celos, desengaños e ilusiones con el rumor incesante de las olas. Una obra conmovedora sobre la memoria, la ternura y la reconciliación. (En español)<br><br>Coauspiciada por Miami-Dade County Auditorium.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Entradas:</strong> 305.547.5414 | 800.745.3000 | www.miamidadecountyauditorium.org")
]

plays_2017_en = [
    # 1
    (1, "Official Poster Unveiling",
     "Thursday, June 15 | 7:00 - 10:00 pm",
     "TONY CARBONELL | Artist",
     "OFFICIAL POSTER UNVEILING",
     "Meet and greet the Artist | Cocktail Reception",
     "Official unveiling of the poster artwork representing the 32nd International Hispanic Theatre Festival of Miami.<br><br>Co-presented by MIAMI-DADE COUNTY AUDITORIUM | Co-sponsored by BACARDÍ USA.",
     "MDCA's On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
     "(By invitation only)"),
    # 2
    (2, "Educational Component",
     "July 6-23 | After each opening",
     "BEATRIZ J. RIZK, Ph.D. | Educational Program Director",
     "EDUCATIONAL COMPONENT | FORUMS ABOUT EACH OPENING",
     "Dialogue and analysis between creators, casts, and audiences",
     "Discussions and roundtables held after opening performances with casts, directors, and theater scholars.<br><br>At each of the participating theatres.",
     "Festival Theatres | Miami",
     "Free admission with performance ticket"),
    # 3
    (3, "2017 Life Achievement Award Julieta Egurrola",
     "Thursday, July 6 | 8:30 pm (Immediately before the performance)",
     "MEXICO",
     "2017 LIFE ACHIEVEMENT IN THE PERFORMING ARTS AWARD",
     "Honoring Julieta Egurrola",
     "Award honoring Mexican stage, film, and television star Julieta Egurrola for her prolific, lifelong dedication and artistic brilliance.<br><br>Co-presented by INSTITUTO CULTURAL DE MEXICO EN MIAMI & AEROMÉXICO.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "Award ceremony"),
    # 4
    (4, "Something by One Shakespeare",
     "Thursday, Friday, and Saturday; July 6, 7, and 8 | 8:30 pm<br>Sunday, July 9 | 5:00 pm",
     "LOS TRISTES TIGRES | Mexico City, Mexico",
     "ALGO DE UN TAL SHAKESPEARE (Something by One Shakespeare)",
     "Written and directed by Adrián Vázquez",
     "An invitation to play on the stage, to be irreverent. It is an entertainment composed of improvisations on William Shakespeare’s writings, a playful journey through some of the works of the greatest dramatist of all time. It seeks to bring children and young people closer to Elizabethan theater without boredom. (In Spanish)<br><br>Co-sponsored by FONCA México.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Tickets:</strong> 305.949.6722 | 866.949.6722 (toll free) | www.arshtcenter.org"),
    # 5
    (5, "Everything That’s By My Side",
     "Friday and Saturday, July 7 and 8 | 6:00 - 8:30 pm<br>Sunday, July 9 | 3:00 - 4:30 pm",
     "FERNANDO RUBIO | Buenos Aires, Argentina",
     "TODO LO QUE ESTÁ A MI LADO (Everything That’s By My Side)",
     "Written and directed by Fernando Rubio",
     "An intimate and immersive theatrical experience. In individual beds set up in the lobby, an actress and a single spectator share a whispered childhood memory, exploring intimacy, subtle movement, memory's drift, and human connections. (In Spanish)<br><br>Co-sponsored by Miami-Dade County Auditorium.",
     "Miami-Dade County Auditorium Lobby | 2901 West Flagler Street, Miami",
     "<strong>Tickets:</strong> 305.547.5414 | www.miamidadecountyauditorium.org"),
    # 6
    (6, "Precious Stones",
     "Friday and Saturday, July 7 and 8 | 8:30 pm<br>Sunday, July 9 | 5:00 pm",
     "AL FIN Y AL CABO | Marbella, Spain",
     "PIEDRAS PRECIOSAS (Precious Stones)",
     "By Pablo Díaz | Directed by Andrea Chacón Álvarez & Raul Mancilla",
     "In the 1960s, artist Jean Cocteau spent several years in Marbella. Piedras preciosas imagines the relationship between Cocteau and Manuel, a young flamenco dancer, showing their mutual learning and affection. (In Spanish)<br><br>Co-sponsored by Otoclinic, Teloneras, Ayto. Marbella, CCEMiami, and Miami-Dade County Auditorium.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Tickets:</strong> 305.547.5414 | 800.745.3000 (toll free) | www.miamidadecountyauditorium.org"),
    # 7
    (7, "Oedipus",
     "Thursday, Friday, and Saturday; July 13, 14, and 15 | 8:30 pm",
     "MÁRMORE - COMPANHIA DO CHAPITÔ | Lisbon, Portugal",
     "ÉDIPO (Oedipus)",
     "Collective creation from the classic Oedipus of Sophocles | Directed by José Carlos García",
     "Oedipus sets out to escape his inexorable fate of parricide and incest, duel with monsters, and endure tragedies. Companhia do Chapitô recounts this classic Greek tragedy through breathtaking physical comedy in a totally hilarious, inventive way. (In Spanish with English supertitles)<br><br>Co-sponsored by Miami-Dade County Auditorium.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Tickets:</strong> 305.547.5414 | 800.745.3000 (toll free) | www.miamidadecountyauditorium.org"),
    # 8
    (8, "The Monsters",
     "Friday and Saturday, July 14 and 15 | 8:30 pm<br>Sunday, July 16 | 5:00 pm",
     "COMPAÑÍA CRIOLLA | Buenos Aires, Argentina",
     "LOS MONSTRUOS (The Monsters)",
     "Written and directed by Emiliano Dionisi",
     "Claudio and Sandra know their children have unique qualities distinguishing them from the rest. Sure they have behavioral issues and are seldom invited to parties, but only a good parent can protect their offspring from a monstrous world. An internationally acclaimed musical drama. (In Spanish)<br><br>Co-sponsored by Ministerio de Cultura de Buenos Aires and the Argentine Consulate.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Tickets:</strong> 305.949.6722 | 866.949.6722 (toll free) | www.arshtcenter.org"),
    # 9
    (9, "Nests",
     "Saturday, July 15 | 5:00 pm",
     "TELONCILLO TEATRO | Valladolid, Spain",
     "NIDOS (Nests)",
     "Written and directed by Ana Gallego & Ángel Sánchez",
     "A poetic theatrical show featuring live music, sounds, shapes, and vibrant colors inspired by birds and their nests, specially conceived for young children and their families. (In Spanish)<br><br>Co-presented by Key Biscayne Community Center | Co-sponsored by TARGET, INAEM Spain, Key Biscayne Community Foundation, Village of Key Biscayne, and Marlins Foundation.",
     "Island Room, Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
     "Free admission & parking | <strong>Reservations:</strong> 305.365.8900"),
    # 10
    (10, "International Children's Day — Nests",
     "Sunday, July 16 | 2:00 - 7:00 pm",
     "TELONCILLO TEATRO | Valladolid, Spain",
     "INTERNATIONAL CHILDREN'S DAY — NESTS",
     "Written and directed by Ana Gallego & Ángel Sánchez",
     "<strong>2:00-3:00pm</strong> | Arts and crafts, rides, face painting, and distribution of combo meals<br><strong>3:00-4:30pm</strong> | Interactive workshops: acting, dance, voice/music, painting, and puppetry<br><strong>4:45-5:45pm</strong> | Workshop participants' presentation<br><strong>6:00-7:00pm</strong> | PERFORMANCE: <em>Nidos</em> by Teloncillo Teatro and cooking fun with Short Chef.<br><br>Co-sponsored by TARGET, CCEMiami, Junta de Castilla y León, Teatro Calderón, INAEM, Te Veo, Artesa, Marlins Foundation, and United Aliens Artists Foundation.",
     "MDCA’s On.Stage Black Box Theatre | 2901 West Flagler Street, Miami",
     "Free admission and parking | <strong>Information:</strong> 305.547.5414"),
    # 11
    (11, "Forgetting",
     "Thursday, Friday, and Saturday; July 20, 21, and 22 | 8:30 pm<br>Sunday, July 23 | 5:00 pm",
     "TEATRO AVANTE | Miami, Florida, USA (U.S. Premiere)",
     "NOTAS QUE SABEN A OLVIDO (Forgetting)",
     "By Araceli Mariel Arreche | Directed by Mario Ernesto Sánchez",
     "Making use of theater's power to communicate and acknowledging the need to know more about this cognitive disorder, the play explores the complex situation of those living with Alzheimer's, reflecting on affection, memory, and everyday relationships. (In Spanish with English supertitles)<br><br>Co-sponsored by Miami-Dade County Department of Cultural Affairs, National Endowment for the Arts, and State of Florida Division of Cultural Affairs.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Tickets:</strong> 305.949.6722 | 866.949.6722 (toll free) | www.arshtcenter.org"),
    # 12
    (12, "Three Old Seas",
     "Friday and Saturday, July 21 and 22 | 8:30 pm<br>Sunday, July 23 | 5:00 pm",
     "ESCENA NORTE (El Salvador) / RAYUELA TEATRO (Guatemala) / GRUPO TEATRAL BAMBÚ (Honduras)",
     "TRES VIEJOS MARES (Three Old Seas)",
     "By Arístides Vargas | Directed by Arístides Vargas and Charo Francés",
     "Three old men meet by the sea to talk about the twilight of their lives, filled with rivalry, jealousy, disappointment, and illusion against the ocean tides. A moving play on memory, humor, and tender reconciliation. (In Spanish)<br><br>Co-sponsored by Miami-Dade County Auditorium.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Tickets:</strong> 305.547.5414 | 800.745.3000 (toll free) | www.miamidadecountyauditorium.org")
]

def build_plays_html(plays_list, ed_num):
    articles = []
    for p in plays_list:
        articles.append(format_play(p[0], ed_num, p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]))
    return "\n\n".join(articles)

# Write 2016 ES
plays_html_2016_es = build_plays_html(plays_2016_es, 31)
page_2016_es = get_template("es", "2016", 31, plays_html_2016_es)
dir_2016_es = os.path.join(workspace, "es", "archivos-del-festival", "2016")
os.makedirs(dir_2016_es, exist_ok=True)
with open(os.path.join(dir_2016_es, "index.html"), "w", encoding="utf-8") as f:
    f.write(page_2016_es)
print("Wrote es/archivos-del-festival/2016/index.html")

# Write 2016 EN
plays_html_2016_en = build_plays_html(plays_2016_en, 31)
page_2016_en = get_template("en", "2016", 31, plays_html_2016_en)
dir_2016_en = os.path.join(workspace, "en", "archivos-del-festival", "2016")
os.makedirs(dir_2016_en, exist_ok=True)
with open(os.path.join(dir_2016_en, "index.html"), "w", encoding="utf-8") as f:
    f.write(page_2016_en)
print("Wrote en/archivos-del-festival/2016/index.html")

# Write 2017 ES
plays_html_2017_es = build_plays_html(plays_2017_es, 32)
page_2017_es = get_template("es", "2017", 32, plays_html_2017_es)
dir_2017_es = os.path.join(workspace, "es", "archivos-del-festival", "2017")
os.makedirs(dir_2017_es, exist_ok=True)
with open(os.path.join(dir_2017_es, "index.html"), "w", encoding="utf-8") as f:
    f.write(page_2017_es)
print("Wrote es/archivos-del-festival/2017/index.html")

# Write 2017 EN
plays_html_2017_en = build_plays_html(plays_2017_en, 32)
page_2017_en = get_template("en", "2017", 32, plays_html_2017_en)
dir_2017_en = os.path.join(workspace, "en", "archivos-del-festival", "2017")
os.makedirs(dir_2017_en, exist_ok=True)
with open(os.path.join(dir_2017_en, "index.html"), "w", encoding="utf-8") as f:
    f.write(page_2017_en)
print("Wrote en/archivos-del-festival/2017/index.html")

print("All 4 pages for 2016 and 2017 created successfully!")
