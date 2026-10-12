import os

workspace = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF-Miami\IHTF"

def get_template(lang, year, roman, tribute_target, plays_html):
    if lang == "es":
        title = f"{roman} Festival Internacional de Teatro Hispano de Miami ({year}) | Archivos"
        desc = f"Programa oficial de obras presentadas en la {year[-2:]}ª edición del Festival Internacional de Teatro Hispano de Miami ({year}) - Homenaje a {tribute_target}."
        canonical = f"https://vayol-art.github.io/IHTF/es/archivos-del-festival/{year}/"
        en_switch_url = f"../../../en/archivos-del-festival/{year}/"
        header_h2 = f"{roman} FESTIVAL INTERNACIONAL DE TEATRO HISPANO DE MIAMI | HOMENAJE A {tribute_target.upper()}"
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
        edition_suffix = "29th" if year == "2014" else "30th"
        title = f"{roman} International Hispanic Theatre Festival of Miami ({year}) | Archives"
        desc = f"Official program of plays presented at the {edition_suffix} International Hispanic Theatre Festival of Miami ({year}) - A Tribute to {tribute_target}."
        canonical = f"https://vayol-art.github.io/IHTF/en/archivos-del-festival/{year}/"
        es_switch_url = f"../../../es/archivos-del-festival/{year}/"
        header_h2 = f"{roman} INTERNATIONAL HISPANIC THEATRE FESTIVAL OF MIAMI | A TRIBUTE TO {tribute_target.upper()}"
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

# Plays for 2014
plays_2014_es = [
    # 1
    (1, "Calígula, The Musical",
     "Jueves, Viernes y Sábado, 10, 11 y 12 de julio | 8:30 P.M.<br>Domingo 13 de julio | 5:00 P.M.",
     "CIBRIÁN MAHLER CO. | Buenos Aires, Argentina",
     "CALÍGULA, THE MUSICAL",
     "Escrita por Pepe Cibrián Campoy y Ángel Mahler | Dirigida por Pepe Cibrián Campoy",
     "Retrato del poder ilimitado, un canto a la libertad del hombre en su lucha contra un poder omnipotente, omnipresente y asesino.<br><br>Coauspiciada por la Dirección General de Asuntos Culturales, Ministerio de Relaciones Exteriores y Culto, Argentina (Desnudo parcial).",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Entradas:</strong> 305.949.6722 | 866.949.6722 | www.arshtcenter.org"),
    # 2
    (2, "La conducta de la vida",
     "Viernes 11 y 18, y Sábado 12 y 19 de julio | 8:30 P.M.",
     "TEATRO PROMETEO | Miami, Florida, EE. UU.",
     "LA CONDUCTA DE LA VIDA (The Conduct of Life)",
     "Escrita por María Irene Fornés | Dirigida por Joann Yarrow",
     "La política, el poder y los derechos humanos enmarcan una historia en la cual el conflicto doméstico refleja la violencia de la sociedad. (En español con supertítulos en inglés)",
     "Teatro Prometeo, Miami-Dade College, Wolfson Campus | 300 NE 2nd Avenue, Miami",
     "<strong>Entradas:</strong> 305.237.3262 | www.teatroprometeo.org<br>Estacionamiento gratis disponible en MDC Lot #1 en la Calle 5 entre la 2da Avenida y Biscayne Boulevard"),
    # 3
    (3, "Arizona",
     "Sábado 12 de julio | 8:30 P.M.<br>Domingo 13 de julio | 5:00 P.M.",
     "TEATRO DE BABEL | México D.F., México",
     "ARIZONA",
     "Escrita por Juan Carlos Rubio | Dirigida por Ignacio García",
     "Sobre fronteras, migración, estupidez humana y los límites de la manipulación. Un retrato tragicómico de dos almas perdidas en el desierto de la vida.<br><br>Coauspiciada por INBA-Conaculta, Fonca, INAEM, Centro Dramático Nacional, Ocesa y la Embajada de España en México.",
     "Miami-Dade College's Koubek Center Theater | 2705 SW 3rd Street, Miami",
     "<strong>Entradas:</strong> 305.237.3262 | www.teatroprometeo.org<br>$3 de descuento en el estacionamiento del local con la entrada de teatro"),
    # 4
    (4, "Volvió una noche",
     "Lunes 14 de julio | 8:30 P.M.",
     "TEATRO PROMETEO | Miami, Florida, EE. UU.",
     "VOLVIÓ UNA NOCHE (She Returned One Night)",
     "Escrita por Eduardo Rovner | Dirigida por Beatriz J. Rizk",
     "La lucha entre los cambios deseados por los individuos y la persistencia de las tradiciones impuestas por generaciones anteriores. (Lectura dramatizada)",
     "Teatro Prometeo, Miami-Dade College, Wolfson Campus | 300 NE 2nd Avenue, Miami",
     "Entrada gratis | <strong>Información:</strong> 305.237.3262 | www.teatroprometeo.org<br>Estacionamiento gratis disponible en MDC Lot #1 en la Calle 5 entre la 2da Avenida y Biscayne Boulevard"),
    # 5
    (5, "Querido San Antonio",
     "Martes 15 de julio | 8:30 P.M.",
     "TEATRO PROMETEO | Miami, Florida, EE. UU.",
     "QUERIDO SAN ANTONIO (Dear St. Anthony)",
     "Escrita por Patricia Suárez | Dirigida por Beatriz J. Rizk",
     "Las expectativas creadas por una sociedad que empuja a las mujeres a luchar por un estatus tradicional chocan con una realidad que está mejor definida por sus límites que por sus oportunidades. (Lectura dramatizada)",
     "Teatro Prometeo, Miami-Dade College, Wolfson Campus | 300 NE 2nd Avenue, Miami",
     "Entrada gratis | <strong>Información:</strong> 305.237.3262 | www.teatroprometeo.org<br>Estacionamiento gratis disponible en MDC Lot #1 en la Calle 5 entre la 2da Avenida y Biscayne Boulevard"),
    # 6
    (6, "Cádiz en mi corazón",
     "Jueves y Viernes, 17 y 18 de julio | 8:30 P.M.",
     "ALBANTA | Cádiz, España",
     "CÁDIZ EN MI CORAZÓN (Cádiz in My Heart)",
     "Escrita por Abel González Melo | Dirigida por Pepe Bablé",
     "Un viaje imposible, a través de postales, a lugares desconocidos, esforzándose por volver al pasado, por inventar lo que no fue y por adueñarse de su propio destino.<br><br>Coauspiciada por INAEM, Ministerio de Educación, Cultura y Deporte, Gobierno de España.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Entradas:</strong> 305.949.6722 | 866.949.6722 | www.arshtcenter.org"),
    # 7
    (7, "El panfleto del rey y su lacayo",
     "Jueves y Viernes, 17 y 18 de julio | 8:30 P.M.",
     "CACUMEN TEATRO | México D.F., México",
     "EL PANFLETO DEL REY Y SU LACAYO (The Pamphlet of the King and His Footman)",
     "Escrita por Cutberto López | Dirigida por Angélica Rogel",
     "El mundo de los que nos gobiernan se retrata de manera cómica y desenfadada, descubriendo por debajo la lucha desnuda por el poder.<br><br>Coauspiciada por INBA - CONACULTA.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Entradas:</strong> 305.547.5414 | 800.745.3000 | www.miamidadecountyauditorium.org"),
    # 8
    (8, "Bromas y lamentos",
     "Viernes y Sábado, 18 y 19 de julio | 10:00 P.M.",
     "TEATRO MUSICAL CONTEMPORÁNEO | Buenos Aires, Argentina",
     "BROMAS Y LAMENTOS (Jokes and Laments)",
     "Escrita y dirigida por Marcelo Lombardero",
     "En una moderna puesta en escena, Lombardero entabla un diálogo entre la música del Barroco temprano y las ideas teatrales de vanguardia.<br><br>En colaboración con Florida Grand Opera y Miami-Dade County Auditorium.",
     "Miami-Dade County Auditorium Lobby | 2901 West Flagler Street, Miami",
     "<strong>Entradas:</strong> 305.547.5414 | www.miamidadecountyauditorium.org"),
    # 9
    (9, "Guyi Guyi",
     "Sábado 19 de julio | 5:45 P.M.",
     "PERIFERIA TEATRO | Murcia, España",
     "GUYI GUYI",
     "Escrita por JM Quiñonero y María Socorro García | Dirigida por JM Quiñonero",
     "La búsqueda de la identidad, el miedo a las diferencias y los prejuicios que enfrentan a quienes se comportan de maneras distintas a lo que esperamos. (Una producción bilingüe para toda la familia)<br><br>En colaboración con Key Biscayne Community Center | Coauspiciada por el Centro Cultural Español de Miami, INAEM, Spain Arts & Culture, Spain USA Foundation, Key Biscayne Community Foundation y Village of Key Biscayne.",
     "Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
     "Entrada y estacionamiento gratis | <strong>Reservaciones:</strong> 305.365.8900"),
    # 10
    (10, "Dinossauros",
     "Sábado 19 de julio | 8:30 P.M.<br>Domingo 20 de julio | 5:00 P.M.",
     "TEATRO CENA | Brasilia, Brasil",
     "DINOSSAUROS (Dinosaurs)",
     "Escrita por Santiago Serrano | Dirigida por Guilherme Reis",
     "Sobre la sensibilidad y la búsqueda de la felicidad en un mundo cada vez más opresivo, trazando un paralelo con los dinosaurios que, para sobrevivir, necesitan crear un futuro posible. (En portugués con supertítulos en español)",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Entradas:</strong> 305.949.6722 | 866.949.6722 | www.arshtcenter.org"),
    # 11
    (11, "El loco y la camisa",
     "Sábado 19 de julio | 8:30 P.M.<br>Domingo 20 de julio | 5:00 P.M.",
     "BANFIELD TEATRO ENSAMBLE | Buenos Aires, Argentina",
     "EL LOCO Y LA CAMISA (The Madman and the Shirt)",
     "Escrita y dirigida por Nelson Valente",
     "¿Quién está cuerdo y quién está loco? No hay mayor locura que vivir en una mentira constante. La irrealidad enloquece y corrompe.<br><br>Coauspiciada por el Instituto Cultural de la Provincia de Buenos Aires.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Entradas:</strong> 305.547.5414 | 800.745.3000 | www.miamidadecountyauditorium.org"),
    # 12
    (12, "La visita",
     "Sábado 19 de julio | 8:30 P.M.<br>Domingo 20 de julio | 5:00 P.M.",
     "UROC TEATRO | Madrid, España",
     "LA VISITA (The Visit)",
     "Escrita y dirigida por Antonio Muñoz de Mesa",
     "Lo grotesco de un feroz combate entre la moral y la avaricia. Los principios éticos pasan a un segundo plano cuando compiten con el implacable afán de lucro.<br><br>Coauspiciada por la Comunidad de Madrid, Ministerio de Cultura.",
     "Miami-Dade College's Koubek Center Theater | 2705 SW 3rd Street, Miami",
     "<strong>Entradas:</strong> 305.237.3262 | www.teatroprometeo.org<br>$3 de descuento en el estacionamiento del local con la entrada de teatro"),
    # 13
    (13, "Día Internacional del Niño - Guyi Guyi",
     "Domingo 20 de julio | 2:00-7:00 P.M.",
     "PERIFERIA TEATRO | Murcia, España",
     "DÍA INTERNACIONAL DEL NIÑO — GUYI GUYI",
     "Escrita por JM Quiñonero y María Socorro García | Dirigida por JM Quiñonero",
     "<strong>2:00-2:45 P.M.</strong> | Manualidades, atracciones, pintacaritas y distribución de meriendas<br><strong>3:00-4:30 P.M.</strong> | Talleres: actuación, danza, voz/música, pintura y títeres<br><strong>4:45-5:45 P.M.</strong> | Presentación de los participantes de los talleres<br><strong>6:00-7:00 P.M.</strong> | FUNCIÓN: <em>Guyi Guyi</em>.<br><br>La búsqueda de la identidad, el miedo a las diferencias y los prejuicios que enfrentan a quienes se comportan de maneras distintas a lo que esperamos. Una producción bilingüe para toda la familia.<br><br>En colaboración con Miami Dade College, InterAmerican Campus | Coauspiciada por Centro Cultural Español de Miami, INAEM, Spain Arts & Culture, Spain USA Foundation y Marlins Foundation. Auspiciado por TARGET.",
     "Miami-Dade College, InterAmerican Campus | 627 SW 27th Avenue, Miami",
     "Entrada y estacionamiento gratis | <strong>Información:</strong> 305.237.6186"),
    # 14
    (14, "Años difíciles",
     "Jueves, Viernes y Sábado, 24, 25 y 26 de julio | 8:30 P.M.<br>Domingo 27 de julio | 5:00 P.M.",
     "TEATRO AVANTE | Miami, Florida, EE. UU.",
     "AÑOS DIFÍCILES (Difficult Years)",
     "Escrita por Roberto Cossa | Dirigida por Mario Ernesto Sánchez",
     "Una historia donde abundan las alusiones y metáforas, así como un humor negro, absurdo y, por momentos, una hipocresía engañosa. (En español con supertítulos en inglés)<br><br>Coauspiciada por Miami-Dade County Dept. of Cultural Affairs, National Endowment for the Arts y State of Florida Division of Cultural Affairs.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Entradas:</strong> 305.949.6722 | 866.949.6722 | www.arshtcenter.org"),
    # 15
    (15, "¡Gaudeamus!",
     "Viernes y Sábado, 25 y 26 de julio | 8:30 P.M.",
     "LA CHANA TEATRO | Salamanca, España",
     "¡GAUDEAMUS!",
     "Escrita por Miguel de Cervantes y Jaime Santos | Dirigida por Jaime Santos",
     "Una producción divertida, dinámica, hilarante y profunda en la que un «juego de objetos» expande y enriquece la historia.<br><br>Coauspiciada por Agencia Española de Cooperación Internacional para el Desarrollo (AECID), Ministerio de Asuntos Exteriores, Gobierno de España.",
     "Teatro Prometeo, Miami-Dade College, Wolfson Campus | 300 NE 2nd Avenue, Miami",
     "<strong>Entradas:</strong> 305.237.3262 | www.teatroprometeo.org<br>Estacionamiento gratis disponible en MDC Lot #1 en la Calle 5 entre la 2da Avenida y Biscayne Boulevard"),
    # 16
    (16, "Federico... ¡Ay, clavel!",
     "Viernes 25 de julio, 1, 8, 15 de agosto, y Sábado 26 de julio, 2, 9, 16 de agosto | 8:30 P.M.",
     "ADRIANA BARRAZA BLACK BOX & NOBARTE | Miami, Florida, EE. UU.",
     "FEDERICO... ¡AY, CLAVEL!",
     "Escrita y dirigida por Neher Jaqueline Briceño",
     "Dos mujeres se reinventan en una encarnizada lucha por un espacio que a ambas pertenece, en un conflicto entre la poesía y la danza, entre el personaje y la música.",
     "Adriana Barraza Black Box | 3100 NW 72nd Avenue, Suite 127, Miami",
     "<strong>Entradas:</strong> 305.436.2916 | 305.436.3916 | www.abactingstudio.com"),
    # 17
    (17, "Otelo",
     "Sábado 26 de julio | 8:30 P.M.<br>Domingo 27 de julio | 5:00 P.M.",
     "COMPAÑÍA DE TEATRO VIAJEINMÓVIL | Santiago, Chile",
     "OTELO (Othello)",
     "Libremente adaptada y dirigida por Christian Ortega, Teresita Iacobelli y Jaime Lorca",
     "La tragedia de amor más famosa de todos los tiempos, representada de forma sencilla, enfocándose en la asombrosa sincronización física de los movimientos de los dos actores.",
     "Miami-Dade College's Koubek Center Theater | 2705 SW 3rd Street, Miami",
     "<strong>Entradas:</strong> 305.237.3262 | www.teatroprometeo.org<br>$3 de descuento en el estacionamiento del local con la entrada de teatro")
]

plays_2014_en = [
    # 1
    (1, "Calígula, The Musical",
     "Thursday, Friday, and Saturday; July 10, 11, and 12 | 8:30pm<br>Sunday, July 13 | 5:00pm",
     "CIBRIÁN MAHLER CO. | Buenos Aires, Argentina",
     "CALÍGULA, THE MUSICAL",
     "Written by Pepe Cibrián Campoy and Ángel Malher | Directed by Pepe Cibrián Campoy",
     "A portrait of unlimited power, a song to human freedom in its struggle against omnipotent, omnipresent and murderous power.<br><br>Co-sponsored by Dirección General de Asuntos Culturales, Ministerio de Relaciones Exteriores y Culto, Argentina (Brief nudity).",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Tickets:</strong> 305.949.6722 | 866.949.6722 (toll free) | www.arshtcenter.org"),
    # 2
    (2, "The Conduct of Life",
     "Friday, July 11 and 18, and Saturday, July 12 and 19 | 8:30pm",
     "TEATRO PROMETEO | Miami, Florida, USA",
     "LA CONDUCTA DE LA VIDA (The Conduct of Life)",
     "Written by María Irene Fornés | Directed by Joann Yarrow",
     "Politics, power and human rights frame a story in which domestic conflict mirrors societal violence. (In Spanish with English supertitles)",
     "Teatro Prometeo, Miami-Dade College, Wolfson Campus | 300 NE 2nd Avenue, Miami",
     "<strong>Tickets:</strong> 305.237.3262 | www.teatroprometeo.org<br>Free parking available at MDC Lot #1 on 5th Street between 2nd Avenue and Biscayne Boulevard"),
    # 3
    (3, "Arizona",
     "Saturday, July 12 | 8:30pm<br>Sunday, July 13 | 5:00pm",
     "TEATRO DE BABEL | Mexico D.F., Mexico",
     "ARIZONA",
     "Written by Juan Carlos Rubio | Directed by Ignacio García",
     "About borders, migration, human stupidity and the limits of manipulation. A tragicomic portrait of two souls lost in the desert of life.<br><br>Co-sponsored by Mexico's INBA-Conaculta, Fonca, INAEM, Centro Dramático Nacional, Ocesa, and the Spanish Embassy in Mexico.",
     "Miami-Dade College's Koubek Center Theater | 2705 SW 3rd Street, Miami",
     "<strong>Tickets:</strong> 305.237.3262 | www.teatroprometeo.org<br>$3 discounted parking on premises with theatre ticket"),
    # 4
    (4, "She Returned One Night",
     "Monday, July 14 | 8:30pm",
     "TEATRO PROMETEO | Miami, Florida, USA",
     "VOLVIÓ UNA NOCHE (She Returned One Night)",
     "Written by Eduardo Rovner | Directed by Beatriz J. Rizk",
     "The struggle between the changes sought by individuals and the persistence of traditions imposed by earlier generations. (Staged reading)",
     "Teatro Prometeo, Miami-Dade College, Wolfson Campus | 300 NE 2nd Avenue, Miami",
     "Free admission | <strong>Information:</strong> 305.237.3262 | www.teatroprometeo.org<br>Free parking available at MDC Lot #1 on 5th Street between 2nd Avenue and Biscayne Boulevard"),
    # 5
    (5, "Dear St. Anthony",
     "Tuesday, July 15 | 8:30pm",
     "TEATRO PROMETEO | Miami, Florida, USA",
     "QUERIDO SAN ANTONIO (Dear St. Anthony)",
     "Written by Patricia Suárez | Directed by Beatriz J. Rizk",
     "The expectations created by a society that pushes women to strive for traditional status clash with a reality that is better defined by its limits than by its opportunities. (Staged reading)",
     "Teatro Prometeo, Miami-Dade College, Wolfson Campus | 300 NE 2nd Avenue, Miami",
     "Free admission | <strong>Information:</strong> 305.237.3262 | www.teatroprometeo.org<br>Free parking available at MDC Lot #1 on 5th Street between 2nd Avenue and Biscayne Boulevard"),
    # 6
    (6, "Cádiz in My Heart",
     "Thursday and Friday, July 17 and 18 | 8:30pm",
     "ALBANTA | Cádiz, Spain",
     "CÁDIZ EN MI CORAZÓN (Cádiz in My Heart)",
     "Written by Abel González Melo | Directed by Pepe Bablé",
     "An impossible journey, via postcards, to places unknown, striving to return to the past, to invent what was not and to own one's fate.<br><br>Co-sponsored by INAEM, Ministerio de Educación, Cultura y Deporte, Gobierno de España.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Tickets:</strong> 305.949.6722 | 866.949.6722 (toll free) | www.arshtcenter.org"),
    # 7
    (7, "The Pamphlet of the King and His Footman",
     "Thursday and Friday, July 17 and 18 | 8:30pm",
     "CACUMEN TEATRO | Mexico D.F., Mexico",
     "EL PANFLETO DEL REY Y SU LACAYO (The Pamphlet of the King and His Footman)",
     "Written by Cutberto López | Directed by Angélica Rogel",
     "The world of those who govern us is depicted in a comic, unabashed manner, uncovering the naked struggle for power underneath.<br><br>Co-sponsored by INBA - CONACULTA.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Tickets:</strong> 305.547.5414 | 800.745.3000 (toll free) | www.miamidadecountyauditorium.org"),
    # 8
    (8, "Jokes and Laments",
     "Friday and Saturday, July 18 and 19 | 10:00pm",
     "TEATRO MUSICAL CONTEMPORÁNEO | Buenos Aires, Argentina",
     "BROMAS Y LAMENTOS (Jokes and Laments)",
     "Written and directed by Marcelo Lombardero",
     "In a modern production, Lombardero sets up a dialogue between early Baroque music and avant-garde theatrical ideas.<br><br>In collaboration with the Florida Grand Opera and Miami-Dade County Auditorium.",
     "Miami-Dade County Auditorium Lobby | 2901 West Flagler Street, Miami",
     "<strong>Tickets:</strong> 305.547.5414 | www.MiamiDadeCountyAuditorium.org"),
    # 9
    (9, "Guyi Guyi",
     "Saturday, July 19 | 5:45pm",
     "PERIFERIA TEATRO | Murcia, Spain",
     "GUYI GUYI",
     "Written by JM Quiñonero and María Socorro García | Directed by JM Quiñonero",
     "The search for identity, the fear of differences and the prejudices that face those who behave in ways other than what we expect. (A bilingual production for the entire family)<br><br>In collaboration with the Key Biscayne Community Center | Co-sponsored by Centro Cultural Español de Miami, INAEM, Spain Arts & Culture, Spain USA Foundation, Key Biscayne Community Foundation, and the Village of Key Biscayne.",
     "Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
     "Free admission and parking | <strong>Reservations:</strong> 305.365.8900"),
    # 10
    (10, "Dinosaurs",
     "Saturday, July 19 | 8:30pm<br>Sunday, July 20 | 5:00pm",
     "TEATRO CENA | Brasília, Brazil",
     "DINOSSAUROS (Dinosaurs)",
     "Written by Santiago Serrano | Directed by Guilherme Reis",
     "About sensitivity and the quest for happiness in an increasingly oppressive world, drawing a parallel with dinosaurs who, to survive, need to create a possible future. (In Portuguese with Spanish supertitles)",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Tickets:</strong> 305.949.6722 | 866.949.6722 (toll free) | www.arshtcenter.org"),
    # 11
    (11, "The Madman and the Shirt",
     "Saturday, July 19 | 8:30pm<br>Sunday, July 20 | 5:00pm",
     "BANFIELD TEATRO ENSAMBLE | Buenos Aires, Argentina",
     "EL LOCO Y LA CAMISA (The Madman and the Shirt)",
     "Written and directed by Nelson Valente",
     "Who is sane and who is insane? There is no greater madness than to live a constant lie. Unreality maddens and corrupts.<br><br>Co-sponsored by Instituto Cultural de la Provincia de Buenos Aires.",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Tickets:</strong> 305.547.5414 | 800.745.3000 (toll free) | www.miamidadecountyauditorium.org"),
    # 12
    (12, "The Visit",
     "Saturday, July 19 | 8:30pm<br>Sunday, July 20 | 5:00pm",
     "UROC TEATRO | Madrid, Spain",
     "LA VISITA (The Visit)",
     "Written and directed by Antonio Muñoz de Mesa",
     "The grotesqueness of a fierce combat between morality and greed. Ethical principles come in second when vying with the implacable profit motive.<br><br>Co-sponsored by Comunidad de Madrid, Ministerio de Cultura.",
     "Miami-Dade College's Koubek Center Theater | 2705 SW 3rd Street, Miami",
     "<strong>Tickets:</strong> 305.237.3262 | www.teatroprometeo.org<br>$3 discounted parking on premises with theatre ticket"),
    # 13
    (13, "International Children's Day - Guyi Guyi",
     "Sunday, July 20 | 2:00-7:00pm",
     "PERIFERIA TEATRO | Murcia, Spain",
     "INTERNATIONAL CHILDREN'S DAY — GUYI GUYI",
     "Written by JM Quiñonero and María Socorro García | Directed by JM Quiñonero",
     "<strong>2:00-2:45pm</strong> | Arts and crafts, rides, face painting, and distribution of combo meals<br><strong>3:00-4:30pm</strong> | Workshops: acting, dance, voice/music, painting, and puppetry<br><strong>4:45-5:45pm</strong> | Presentation by workshop participants<br><strong>6:00-7:00pm</strong> | PERFORMANCE: <em>Guyi Guyi</em>.<br><br>The search for identity, the fear of differences and the prejudices that face those who behave in ways other than what we expect. A bilingual production for the entire family.<br><br>In collaboration with Miami Dade College, InterAmerican Campus | Co-sponsored by Centro Cultural Español de Miami, INAEM, Spain Arts & Culture, Spain USA Foundation, and the Marlins Foundation. Sponsored by TARGET.",
     "Miami-Dade College, InterAmerican Campus | 627 SW 27th Avenue, Miami",
     "Free admission and parking | <strong>Information:</strong> 305.237.6186"),
    # 14
    (14, "Difficult Years",
     "Thursday, Friday, and Saturday; July 24, 25, and 26 | 8:30pm<br>Sunday, July 27 | 5:00pm",
     "TEATRO AVANTE | Miami, Florida, USA",
     "AÑOS DIFÍCILES (Difficult Years)",
     "Written by Roberto Cossa | Directed by Mario Ernesto Sánchez",
     "A story in which allusions and metaphors abound, as well as absurd, dark humor and, at times, deceitful hypocrisy. (In Spanish with English supertitles)<br><br>Co-sponsored by Miami-Dade County Dept. of Cultural Affairs, National Endowment for the Arts, and the State of Florida Division of Cultural Affairs.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Tickets:</strong> 305.949.6722 | 866.949.6722 (toll free) | www.arshtcenter.org"),
    # 15
    (15, "¡Gaudeamus!",
     "Friday and Saturday, July 25 and 26 | 8:30pm",
     "LA CHANA TEATRO | Salamanca, Spain",
     "¡GAUDEAMUS!",
     "Written by Miguel de Cervantes and Jaime Santos | Directed by Jaime Santos",
     "A fun, dynamic, hilarious and profound production in which a “game of objects” expands and enriches the story.<br><br>Co-sponsored by Agencia Española de Cooperación Internacional para el Desarrollo (AECID), Ministerio de Asuntos Exteriores, Gobierno de España.",
     "Teatro Prometeo, Miami-Dade College, Wolfson Campus | 300 NE 2nd Avenue, Miami",
     "<strong>Tickets:</strong> 305.237.3262 | www.teatroprometeo.org<br>Free parking available at MDC Lot #1 on 5th Street between 2nd Avenue and Biscayne Boulevard"),
    # 16
    (16, "Federico... ¡Ay, clavel!",
     "Friday, July 25, August 1, 8, 15, and Saturday, July 26, August 2, 9, 16 | 8:30pm",
     "ADRIANA BARRAZA BLACK BOX & NOBARTE | Miami, Florida, USA",
     "FEDERICO... ¡AY, CLAVEL!",
     "Written and directed by Neher Jaqueline Briceño",
     "Two women reinvent themselves in a bitter struggle for a space that belongs to both, in a conflict between poetry and dance, between character and music.",
     "Adriana Barraza Black Box | 3100 NW 72nd Avenue, Suite 127, Miami",
     "<strong>Tickets:</strong> 305.436.2916 | 305.436.3916 | www.abactingstudio.com"),
    # 17
    (17, "Othello",
     "Saturday, July 26 | 8:30pm<br>Sunday, July 27 | 5:00pm",
     "COMPAÑÍA DE TEATRO VIAJEINMÓVIL | Santiago, Chile",
     "OTELO (Othello)",
     "Freely adapted and directed by Christian Ortega, Teresita Iacobelli, and Jaime Lorca",
     "The most famous love tragedy of all times, simply performed, focusing on the amazingly synchronized physical movements of the two actors.",
     "Miami-Dade College's Koubek Center Theater | 2705 SW 3rd Street, Miami",
     "<strong>Tickets:</strong> 305.237.3262 | www.teatroprometeo.org<br>$3 discounted parking on premises with theatre ticket")
]

# Plays for 2015
plays_2015_es = [
    # 1
    (1, "Peace Transcends",
     "Jueves, Viernes y Sábado, 9, 10 y 11 de julio | 8:30 P.M.<br>Domingo 12 de julio | 5:00 P.M.",
     "VIVER BRASIL DANCE COMPANY | Los Ángeles, California, EE. UU. / Brasil",
     "PEACE TRANSCENDS",
     "Coreografiada por Vera Passos, Rosangela Silvestre, Shelby Williams Gonzalez y Luiz Badaró",
     "Cuatro impactantes obras de danza-teatro afrobrasileño. Homenaje a Nancy de Souza e Silva (Dona Cici), sabia anciana de la cultura candomblé, celebra la paz, la ancestralidad, las fuerzas de la naturaleza y el poder de las mujeres. Paisajes sonoros creativos y atractivos bailes de forró cautivan al público con una fuerza física incontenible, poder, pasión y exuberancia.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Entradas:</strong> 305.949.6722 | 866.949.6722 | www.arshtcenter.org (Danza-teatro)"),
    # 2
    (2, "Cena para seis",
     "Viernes y Sábado, 10 y 11 de julio | 8:30 P.M.",
     "TEATRO PROMETEO | Miami, Florida, EE. UU.",
     "CENA PARA SEIS (Dinner for Six)",
     "Escrita por Cristina Rebull | Dirigida por Joann M. Yarrow y Cristina Rebull",
     "Teatro del absurdo con toques de comedia y suspenso. Seis personas son invitadas anónimamente a una cena, donde uno de ellos anuncia la muerte del «gordo». Cualquiera de ellos podría ser el asesino. La víctima deja de ser víctima y se convierte en acusada en un juicio donde el juez es la conciencia social y ética de los personajes y el público. (En español con supertítulos en inglés)",
     "Teatro Prometeo, Miami-Dade College, Wolfson Campus | 300 NE 2nd Avenue, Miami",
     "<strong>Entradas:</strong> 305.237.3262 | http://cenaparaseis.brownpapertickets.com<br>Estacionamiento gratis disponible en MDC Lot #1 en la Calle 5 entre la 2da Avenida y Biscayne Boulevard"),
    # 3
    (3, "Los más solos",
     "Viernes y Sábado, 10 y 11 de julio | 8:30 P.M.<br>Domingo 12 de julio | 5:00 P.M.",
     "TEATRO DEL AZORO | San Salvador, El Salvador",
     "LOS MÁS SOLOS (The Loneliest)",
     "Escrita y dirigida por Egly Larreynaga y Luis Felpeto",
     "Cuatro reclusos enfermos mentales, víctimas de una dura guerra civil en su juventud y ahora encerrados en un centro psiquiátrico, son el reflejo de una sociedad violenta y desquiciada. Bienvenidos al pabellón psiquiátrico del penal de Soyapango. (En español)",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Entradas:</strong> 305.547.5414 | 800.745.3000 | www.miamidadecountyauditorium.org"),
    # 4
    (4, "BR-Trans",
     "Viernes y Sábado, 10 y 11 de julio | 8:30 P.M.<br>Domingo 12 de julio | 5:00 P.M.",
     "COLECTIVO ARTÍSTICO AS TRAVESTIDAS | Fortaleza y Porto Alegre, Brasil",
     "BR-TRANS",
     "Escrita por Silvero Pereira | Dirigida por Jezebel De Carli",
     "Abordando el papel de la familia, la escuela, la religión, la política y el arte en la comunidad transgénero, la obra retrata la vida de travestis y transformistas a través del teatro documental. BR-TRANS trata sobre hechos, sobre la realidad, y presenta a un personaje del «trans-Brasil», configurado a partir de la convergencia y el desplazamiento entre el noreste y el sur de Brasil. (En portugués con supertítulos en español)",
     "Koubek Theatre | 2705 SW 3rd Street, Miami",
     "<strong>Entradas:</strong> http://www.brownpapertickets.com/event/1567092 | 305.445.8877<br>Valet Parking: $5"),
    # 5
    (5, "Simulacro de idilio",
     "Viernes y Sábado, 17 y 18 de julio | 8:30 P.M.<br>Domingo 19 de julio | 5:00 P.M.",
     "TEATRO DE BABEL & DRAMAFEST | Ciudad de México, México",
     "SIMULACRO DE IDILIO (A Simulated Romance)",
     "Escrita y dirigida por David Gaitán",
     "Un maestro de secundaria parece comprometido a observar el código moral de la sociedad en la que vive. Ante la dificultad de encontrar trabajo y el inminente colapso de su familia, el sistema le ofrece la oportunidad de salvarse corrompiéndose. No terminará bien. (En español)",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Entradas:</strong> 305.949.6722 | 866.949.6722 | www.arshtcenter.org"),
    # 6
    (6, "Swallows / Golondrinas",
     "Viernes y Sábado, 17 y 18 de julio | 8:30 P.M.<br>Domingo 19 de julio | 5:00 P.M.",
     "SINTEATROS INTIMUS | Nueva York, Nueva York, EE. UU. / Venezuela",
     "SWALLOWS (Golondrinas)",
     "Escrita y dirigida por Aminta de Lara",
     "En una época de intensas divisiones partidistas y manifestaciones callejeras multitudinarias tanto a favor como en contra del gobierno, dos hermanas se ven obligadas a analizar a fondo su relación con su difunto padre. Un período oscuro de su infancia alimenta la confrontación entre ambas. (En inglés con supertítulos en español)",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Entradas:</strong> 305.547.5414 | 800.745.3000 | www.miamidadecountyauditorium.org"),
    # 7
    (7, "Apple of My Eye",
     "Viernes y Sábado, 17 y 18 de julio | 8:30 P.M.<br>Domingo 19 de julio | 5:00 P.M.",
     "NETTLES ARTISTS COLLECTIVE | Nueva York, Nueva York, EE. UU. / Brasil",
     "APPLE OF MY EYE (Menina dos Meus Olhos)",
     "Escrita por Tathiana Piancastelli | Dirigida por Debora Balardini",
     "Escrita y representada por una persona con síndrome de Down y con un elenco de diez actores, Apple of My Eye cuenta la historia de una joven que busca el amor y la aceptación social. La obra conecta texto, técnicas vocales, multimedia y teatro físico para promover una visión sin prejuicios de los demás y demostrar que la genialidad y la originalidad no son exclusivas de ciertos grupos. (En portugués con supertítulos en inglés)",
     "Koubek Theatre | 2705 SW 3rd Street, Miami",
     "<strong>Entradas:</strong> http://www.brownpapertickets.com/event/1585487 | 305.445.8877<br>Valet Parking: $5"),
    # 8
    (8, "Zarzuguiñol",
     "Sábado 18 de julio | 5:45 P.M.",
     "ZARZUGUIÑOL | Madrid, España",
     "ZARZUGUIÑOL, ZARZUELA PARA NIÑOS (A Puppet Zarzuela)",
     "Escrita por Javier Ruiz Gaitán y Melisa de las Heras | Dirigida por Carlos Crooke Llop",
     "El simpático títere Don Hilarión de La Verbena de la Paloma y sus amigos nos trasladan a un mundo maravilloso. Los niños descubrirán a los compositores, libretistas y tradiciones de la opereta española, así como deliciosas historias que les permitirán familiarizarse mejor con este género. Un colorido desfile de los personajes que pueblan tales «zarzuelas»: chulapos, chulapas, marineros, espigadoras, labradores, bellas mujeres y valientes caballeros. (En español)",
     "Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
     "Entrada y estacionamiento gratis | <strong>Reservaciones:</strong> 305.365.8900"),
    # 9
    (9, "Día Internacional del Niño - Zarzuguiñol",
     "Domingo 19 de julio | 2:00-7:00 P.M.",
     "ZARZUGUIÑOL | Madrid, España",
     "DÍA INTERNACIONAL DEL NIÑO — ZARZUGUIÑOL, ZARZUELA PARA NIÑOS",
     "Escrita por Javier Ruiz Gaitán y Melisa de las Heras | Dirigida por Carlos Crooke Llop",
     "<strong>2:00-3:00 P.M.</strong> | Manualidades, atracciones, pintacaritas y distribución de meriendas<br><strong>3:00-4:30 P.M.</strong> | Talleres: actuación, danza, voz/música, pintura y títeres<br><strong>4:30-5:30 P.M.</strong> | Presentación de los participantes de los talleres<br><strong>6:00-7:00 P.M.</strong> | FUNCIÓN: <em>Zarzuguiñol, zarzuela para niños</em> (En español).<br><br>El simpático títere Don Hilarión de La Verbena de la Paloma y sus amigos nos trasladan a un mundo maravilloso. Los niños descubrirán a los compositores, libretistas y tradiciones de la opereta española, así como deliciosas historias que les permitirán familiarizarse mejor con este género.",
     "InterAmerican Campus, Miami-Dade College | 627 SW 27th Avenue, Miami",
     "Entrada y estacionamiento gratis | <strong>Información:</strong> 305.237.6186"),
    # 10
    (10, "Alguna cosita que alivie el sufrir",
     "Jueves, Viernes y Sábado, 23, 24 y 25 de julio | 8:30 P.M.<br>Domingo 26 de julio | 5:00 P.M.",
     "TEATRO AVANTE | Miami, Florida, EE. UU.",
     "ALGUNA COSITA QUE ALIVIE EL SUFRIR (A Little Something to Ease the Pain)",
     "Escrita por René R. Alomá | Dirigida por Mario Ernesto Sánchez",
     "El exilio, ese plato agridulce aderezado con la nostalgia de los que se van y la añoranza de los que se quedan, lleva en sí logros y renuncias, beneficios y sacrificios, esperanza y resignación. Los que se van y los que se quedan vivirán siempre buscando alguna cosita que alivie el sufrir. (En español con supertítulos en inglés)",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Entradas:</strong> 305.949.6722 | 866.949.6722 | www.arshtcenter.org"),
    # 11
    (11, "Príncipe azul",
     "Jueves y Viernes, 23 y 24 de julio | 8:30 P.M.",
     "ADRIANA BARRAZA BLACK BOX & NOBARTE | Miami, Florida, EE. UU.",
     "PRÍNCIPE AZUL (Prince Charming)",
     "Escrita por Eugenio Griffero | Dirigida por Neher Jaqueline Briceño",
     "Un pacto para reencontrarse en 50 años y una fecha grabada a fuego en dos corazones, sorprendentes en sus peculiaridades, desafíos y temores. Dos seres atrapados en el hechizo de creerse iguales 50 años después, cuando inevitablemente han dejado de ser lo que alguna vez fueron. (En español)",
     "Adriana Barraza Black Box | 3100 NW 72nd Avenue, Suite 127, Miami",
     "<strong>Entradas:</strong> 305.436.2916 | www.abactingstudio.com<br>Estacionamiento gratis"),
    # 12
    (12, "Escriba su nombre aquí",
     "Viernes y Sábado, 24 y 25 de julio | 8:30 P.M.<br>Domingo 26 de julio | 5:00 P.M.",
     "CUARTO Y MITAD TEATRO | Madrid, España",
     "ESCRIBA SU NOMBRE AQUÍ (Write Your Name Here)",
     "Escrita y dirigida por María Prado y Fernando de Retes",
     "Fruto de una experimentación teatral que busca en las zonas fronterizas formas de vinculación más allá de la nacionalidad, el género, la sexualidad, la religión, las filias y las fobias. ¿Y si pudieras elegir tu nacionalidad a través del servicio de atención al cliente? ¿Y si lo que te define es un número? ¿O tu rarísimo nombre? (En español con supertítulos en inglés)",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Entradas:</strong> 305.547.5414 | 800.745.3000 | www.miamidadecountyauditorium.org"),
    # 13
    (13, "EX – Que revienten los actores",
     "Viernes y Sábado, 24 y 25 de julio | 8:30 P.M.<br>Domingo 26 de julio | 5:00 P.M.",
     "COMPLOT | Montevideo, Uruguay",
     "EX – QUE REVIENTEN LOS ACTORES (EX – To Hell With the Actors)",
     "Escrita y dirigida por Gabriel Calderón",
     "La historia de una niña con un dolor que creció con el tiempo, una necesidad que se profundizó día a día y un problema que estalló en la cara de aquellos que no quisieron escuchar. Esta es la historia de una familia que se reúne en una Navidad después de muchos años separados. (En español con supertítulos en inglés)",
     "Koubek Theater | 2705 SW 3rd Street, Miami",
     "<strong>Entradas:</strong> http://www.brownpapertickets.com/event/1677791 | 305.445.8877<br>Valet Parking: $5")
]

plays_2015_en = [
    # 1
    (1, "Peace Transcends",
     "Thursday, Friday, and Saturday; July 9, 10, and 11 | 8:30pm<br>Sunday, July 12 | 5:00pm",
     "VIVER BRASIL DANCE COMPANY | Los Angeles, California, USA / Brazil",
     "PEACE TRANSCENDS",
     "Choreographed by Vera Passos, Rosangela Silvestre, Shelby Williams Gonzalez, and Luiz Badaró",
     "Four stunning works of Afro-Brazilian dance-theatre. An homage to Nancy de Souza e Silva (Dona Cici), wise elder of the Candomblé culture, it celebrates peace, ancestry, the forces of nature and the power of women. Creative soundscapes and enticing forró dances captivate audiences with irrepressible physicality, power, passion, and exuberance.",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Tickets:</strong> 305.949.6722 | 1.866.949.6722 (toll free) | www.arshtcenter.org (Dance-theatre)"),
    # 2
    (2, "Dinner for Six",
     "Friday and Saturday, July 10 and 11 | 8:30pm",
     "TEATRO PROMETEO | Miami, Florida, USA",
     "CENA PARA SEIS (Dinner for Six)",
     "Written by Cristina Rebull | Directed by Joann M. Yarrow and Cristina Rebull",
     "Theatre of the absurd with touches of comedy and suspense. Six people are anonymously invited to a dinner, where one of them announces the death of “the fat man.” Any one of them could be the killer. The victim stops being the victim and becomes the defendant at a trial in which the judge is the social and ethical conscience of the characters and the audience. (In Spanish with English supertitles)",
     "Teatro Prometeo, Miami-Dade College, Wolfson Campus | 300 NE 2nd Avenue, Miami",
     "<strong>Tickets:</strong> 305.237.3262 | http://cenaparaseis.brownpapertickets.com<br>Free parking available at MDC Lot #1 on 5th Street between 2nd Avenue and Biscayne Boulevard"),
    # 3
    (3, "The Loneliest",
     "Friday and Saturday, July 10 and 11 | 8:30pm<br>Sunday, July 12 | 5:00pm",
     "TEATRO DEL AZORO | San Salvador, El Salvador",
     "LOS MÁS SOLOS (The Loneliest)",
     "Written and directed by Egly Larreynaga and Luis Felpeto",
     "Four mentally ill convicts, victims of a harsh civil war in their youth and now shut away in a psychiatric facility, are reflections of a violent and insane society. Welcome to the psychiatric ward at Soyapango prison. (In Spanish)",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Tickets:</strong> 305.547.5414 | 800.745.3000 (toll free) | www.miamidadecountyauditorium.org"),
    # 4
    (4, "BR-Trans",
     "Friday and Saturday, July 10 and 11 | 8:30pm<br>Sunday, July 12 | 5:00pm",
     "COLECTIVO ARTÍSTICO AS TRASVESTIDAS | Fortaleza & Porto Alegre, Brazil",
     "BR-TRANS",
     "Written by Silvero Pereira | Directed by Jezebel De Carli",
     "Addressing the role of family, school, religion, politics and art in the transgender community, the play depicts the lives of transvestites and cross-dressing performers through documentary theatre. BR-TRANS is about facts, about reality, and features a character from“trans-Brazil”, fashioned from the convergence of and displacement between northeastern and southern Brazil. (In Portuguese with Spanish supertitles)",
     "Koubek Theatre | 2705 SW 3rd Street, Miami",
     "<strong>Tickets:</strong> http://www.brownpapertickets.com/event/1567092 | 305.445-8877<br>Valet Parking: $5"),
    # 5
    (5, "A Simulated Romance",
     "Friday and Saturday, July 17 and 18 | 8:30pm<br>Sunday, July 19 | 5:00pm",
     "TEATRO DE BABEL & DRAMAFEST | Mexico City, Mexico",
     "SIMULACRO DE IDILIO (A Simulated Romance)",
     "Written and directed by David Gaitán",
     "A middle-school teacher appears committed to observing the moral code of the society in which he lives. Facing the difficulty of finding a job and the imminent collapse of his family, the system offers him the opportunity to save himself by becoming corrupt. It won’t end well. (In Spanish)",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Tickets:</strong> 305.949.6722 | 866.949.6722 (toll free) | www.arshtcenter.org"),
    # 6
    (6, "Swallows",
     "Friday and Saturday, July 17 and 18 | 8:30pm<br>Sunday, July 19 | 5:00 p.m.",
     "SINTEATROS INTIMUS | New York, New York, USA / Venezuela",
     "SWALLOWS (Golondrinas)",
     "Written and directed by Aminta de Lara",
     "At a time of intense partisan divisions and massive street demonstrations both for and against the government, two sisters are forced to take a profound look at their relationship with their dead father. A dark period of their childhood fuels the confrontation between them. (In English with Spanish supertitles)",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Tickets:</strong> 305.547-5414 | 1.800.745-3000 (toll-free) | www.miamidadecountyauditorium.org"),
    # 7
    (7, "Apple of My Eye",
     "Friday and Saturday | July 17 and 18 | 8:30pm<br>Sunday, July 19 | 5:00pm",
     "NETTLES ARTISTS COLLECTIVE | New York, New York, USA / Brazil",
     "APPLE OF MY EYE (Menina dos Meus Olhos)",
     "Written by Tathiana Piancastelli | Directed by Debora Balardini",
     "Written and performed by a person with Down syndrome and featuring a cast of ten actors, Apple of My Eye tells the story of a young woman in search of love and social acceptance. The play connects text, vocal techniques, multimedia and physical theatre to advance a non-judgmental view of others and prove that genius and originality are not exclusive to certain groups. (In Portuguese with English supertitles)",
     "Koubek Theatre | 2705 SW 3rd Street, Miami",
     "<strong>Tickets:</strong> http://www.brownpapertickets.com/event/1585487 | 305.445.8877<br>Valet Parking $5"),
    # 8
    (8, "A Puppet Zarzuela",
     "Saturday, July 18 | 5:45pm",
     "ZARZUGUIÑOL | Madrid, Spain",
     "ZARZUGUIÑOL, ZARZUELA PARA NIÑOS (A Puppet Zarzuela)",
     "Written by Javier Ruiz Gaitán and Melisa de las Heras | Directed by Carlos Crooke Llop",
     "The charming puppet Don Hilarión from La Verbena de la Paloma and his friends transport us to a wonderful world. Children will discover the composers, librettists and traditions of Spanish operettas as well as delightful stories that will better acquaint them with this genre. A colorful parade of the characters that populate such “zarzuelas”: chulapos, chulapas, sailors, gleaners, farmers, beautiful women and valiant gentlemen. (In Spanish)",
     "Key Biscayne Community Center | 10 Village Green Way, Key Biscayne",
     "Free admission and parking | <strong>Reservations:</strong> 305.365.8900"),
    # 9
    (9, "International Children's Day - A Puppet Zarzuela",
     "Sunday, July 19 | 2:00-7:00pm",
     "ZARZUGUIÑOL | Madrid, Spain",
     "INTERNATIONAL CHILDREN'S DAY — ZARZUGUIÑOL, A PUPPET ZARZUELA",
     "Written by Javier Ruiz Gaitán & Melisa de las Heras | Directed by Carlos Crooke Llop",
     "<strong>2:00-3:00pm</strong> | Arts and crafts, rides, face painting and distribution of combo meals<br><strong>3:00-4:30pm</strong> | Workshops: acting, dance, voice/music, painting and puppetry<br><strong>4:30-5:30pm</strong> | Presentation by workshop participants<br><strong>6:00-7:00pm</strong> | PERFORMANCE: <em>Zarzuguiñol, a Puppet Zarzuela</em> (In Spanish).<br><br>The charming puppet Don Hilarión from La Verbena de la Paloma and his friends transport us to a wonderful world. Children will discover the composers, librettists and traditions of Spanish operettas as well as delightful stories that will better acquaint them with this genre.",
     "InterAmerican Campus, Miami-Dade College | 627 SW 27th Avenue, Miami",
     "Free admission and parking | <strong>Information:</strong> 305.237.6186"),
    # 10
    (10, "A Little Something to Ease the Pain",
     "Thursday, Friday, and Saturday; July 23, 24, and 25 | 8:30pm<br>Sunday, July 26 | 5:00pm",
     "TEATRO AVANTE | Miami, Florida, USA",
     "ALGUNA COSITA QUE ALIVIE EL SUFRIR (A Little Something to Ease the Pain)",
     "Written by René R. Alomá | Directed by Mario Ernesto Sánchez",
     "Exile, that bittersweet dish seasoned with the nostalgia of those who leave and the yearning of those who stay, bears in it achievements and renunciations, benefits and sacrifices, hope and resignation. Those who go and those who stay will always live seeking a little something to ease the pain. (In Spanish with English supertitles)",
     "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
     "<strong>Tickets:</strong> 305.949.6722 | 866.949.6722 (toll free) | www.arshtcenter.org"),
    # 11
    (11, "Prince Charming",
     "Thursday and Friday, July 23 and 24 | 8:30pm",
     "ADRIANA BARRAZA BLACK BOX & NOBARTE | Miami, Florida, USA",
     "PRÍNCIPE AZUL (Prince Charming)",
     "Written by Eugenio Griffero | Directed by Neher Jaqueline Briceño",
     "A pact to meet again in 50 years and a date stamped on two hearts, amazing in their peculiarities, challenges and fears. Two beings caught in the spell of believing themselves to be the same 50 years later, when they have inevitably stopped being what they once were. (In Spanish)",
     "Adriana Barraza Black Box | 3100 NW 72nd Avenue, Suite 127, Miami",
     "<strong>Tickets:</strong> 305.436.2916 | www.abactingstudio.com<br>Free parking"),
    # 12
    (12, "Write Your Name Here",
     "Friday and Saturday, July 24 and 25 | 8:30pm<br>Sunday, July 26 | 5:00 p.m.",
     "CUARTO Y MITAD TEATRO | Madrid, Spain",
     "ESCRIBA SU NOMBRE AQUÍ (Write Your Name Here)",
     "Written and directed by María Prado and Fernando de Retes",
     "The product of theatrical experimentation that seeks in border areas forms of engagement beyond nationality, gender, sexuality, religion, philias and phobias. What if you could choose your nationality via customer service? What if what defines you is a number? Or your very strange name? (In Spanish with English supertitles)",
     "On.Stage Black Box Theatre @ Miami-Dade County Auditorium | 2901 West Flagler Street, Miami",
     "<strong>Tickets:</strong> 305.547.5414 | 800.745.3000 (toll free) | www.miamidadecountyauditorium.org"),
    # 13
    (13, "EX – To Hell With the Actors",
     "Friday and Saturday, July 24 and 25 | 8:30pm<br>Sunday, July 26 | 5:00pm",
     "COMPLOT | Montevideo, Uruguay",
     "EX – QUE REVIENTEN LOS ACTORES (EX – To Hell With the Actors)",
     "Written and directed by Gabriel Calderón",
     "The story of a girl with sorrow that grew with time, a need that deepened day by day and a problem that blew up in the face of those who wouldn’t listen. This is the story of a family that comes together one Christmas after many years apart. (In Spanish with English supertitles)",
     "Koubek Theater | 2705 SW 3rd Street, Miami",
     "<strong>Tickets:</strong> http://www.brownpapertickets.com/event/1677791 | 305.445.8877<br>Valet parking $5")
]

def build_plays_html(plays_list, ed_num):
    articles = []
    for p in plays_list:
        articles.append(format_play(p[0], ed_num, p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]))
    return "\n\n".join(articles)

# Build and write 2014 ES
plays_html_2014_es = build_plays_html(plays_2014_es, 29)
page_2014_es = get_template("es", "2014", "XXIX", "Argentina", plays_html_2014_es)
dir_2014_es = os.path.join(workspace, "es", "archivos-del-festival", "2014")
os.makedirs(dir_2014_es, exist_ok=True)
with open(os.path.join(dir_2014_es, "index.html"), "w", encoding="utf-8") as f:
    f.write(page_2014_es)
print("Wrote es/archivos-del-festival/2014/index.html")

# Build and write 2014 EN
plays_html_2014_en = build_plays_html(plays_2014_en, 29)
page_2014_en = get_template("en", "2014", "XXIX", "Argentina", plays_html_2014_en)
dir_2014_en = os.path.join(workspace, "en", "archivos-del-festival", "2014")
os.makedirs(dir_2014_en, exist_ok=True)
with open(os.path.join(dir_2014_en, "index.html"), "w", encoding="utf-8") as f:
    f.write(page_2014_en)
print("Wrote en/archivos-del-festival/2014/index.html")

# Build and write 2015 ES
plays_html_2015_es = build_plays_html(plays_2015_es, 30)
page_2015_es = get_template("es", "2015", "XXX", "Brasil", plays_html_2015_es)
dir_2015_es = os.path.join(workspace, "es", "archivos-del-festival", "2015")
os.makedirs(dir_2015_es, exist_ok=True)
with open(os.path.join(dir_2015_es, "index.html"), "w", encoding="utf-8") as f:
    f.write(page_2015_es)
print("Wrote es/archivos-del-festival/2015/index.html")

# Build and write 2015 EN
plays_html_2015_en = build_plays_html(plays_2015_en, 30)
page_2015_en = get_template("en", "2015", "XXX", "Brazil", plays_html_2015_en)
dir_2015_en = os.path.join(workspace, "en", "archivos-del-festival", "2015")
os.makedirs(dir_2015_en, exist_ok=True)
with open(os.path.join(dir_2015_en, "index.html"), "w", encoding="utf-8") as f:
    f.write(page_2015_en)
print("Wrote en/archivos-del-festival/2015/index.html")

print("All 4 edition pages generated successfully!")
