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
        brand_href = "../../#inicio"
        brand_aria = "IHTF Inicio"
        logo_white_alt = "IHTF 40 Blanco"
        logo_color_alt = "IHTF 40 Color"
        lang_btn_aria = "Cambiar idioma"
        menu_open_aria = "Abrir menú"
        main_nav_aria = "Menú principal"

        lang_dropdown_html = f'''          <div class="lang-dropdown">
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
        brand_href = "../../#home"
        brand_aria = "IHTF Home"
        logo_white_alt = "IHTF 40 White"
        logo_color_alt = "IHTF 40 Colors"
        lang_btn_aria = "Change language"
        menu_open_aria = "Open menu"
        main_nav_aria = "Main menu"

        lang_dropdown_html = f'''          <div class="lang-dropdown">
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
            <a href="../../programa-de-mano/" class="submenu-item">Hand Program</a>
            <a href="../../calendario/" class="submenu-item">Schedule</a>
            <a href="../../eventos-adicionales/" class="submenu-item">Additional Events</a>
            <div class="dropdown-divider"></div>
            <a href="../../dia-internacional-del-nino/" class="submenu-item">International Children's Day</a>
            <a href="../../teatros/" class="submenu-item">Venues</a>
            <a href="../../sponsors/" class="submenu-item">Support IHTF</a>
            <a href="../../archivos-del-festival/" class="submenu-item">Festival Archives</a>
          </div>
        </div>
        <a href="../../contactanos/">CONTACT US</a>
        <div class="nav-dropdown-wrapper">
          <a href="../../nosotros/" class="nav-dropdown-trigger">ABOUT US</a>
          <div class="nav-submenu">
            <a href="../../nosotros/#compania" class="submenu-item">Festival History</a>
            <a href="../../nosotros/#personal" class="submenu-item">Staff</a>
          </div>
        </div>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSczcvvSrHnWwI0TgvGq_Ad9R9uOO-UCv7Eqy5VTrn_HMan4-g/viewform?usp=header" target="_blank">41ST FESTIVAL REGISTRATION</a>'''

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
  <meta property="og:locale" content="{('es_US' if lang == 'es' else 'en_US')}" />
  <meta property="og:site_name" content="Festival Internacional de Teatro Hispano de Miami" />

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
    <a class="brand" href="{brand_href}" aria-label="{brand_aria}">
      <img class="logo-white" src="../../../assets/LOGO_EXPORTS%202/LOGOS_DIGITAL/Web/logo%20blanco.png" alt="{logo_white_alt}" />
      <img class="logo-color" src="../../../assets/LOGO_EXPORTS%202/LOGOS_DIGITAL/Web/logo%20colores.png" alt="{logo_color_alt}" />
    </a>
    <div class="nav-container">
      <nav class="main-nav" aria-label="{main_nav_aria}">
{nav_menu_html}
      </nav>

      <div class="header-actions">
        <div class="lang-selector">
          <button class="lang-btn" onclick="toggleLangDropdown(event)" aria-label="{lang_btn_aria}" aria-expanded="false">
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
{lang_dropdown_html}
        </div>
        <button class="hamburger" aria-label="{menu_open_aria}" aria-expanded="false">
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

        <div class="plays-list">
{plays_html}
        </div>

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
      <div><img src="../../../assets/LOGO_EXPORTS%202/LOGOS_DIGITAL/Web/logo%20blanco.png" alt="{logo_white_alt}" class="footer-logo" /></div>
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

def build_play_article(num, img, alt, dates, company, title, credits, synopsis, venue, contact):
    return f'''          <!-- Obra {num} -->
          <article class="play-item">
            <div class="play-top">
              <div class="play-thumb">
                <img src="{img}" alt="{alt}" loading="lazy" />
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

plays_es = [
    {
        "num": 1,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra1.png",
        "alt": "CARRUSEL",
        "dates": "Miércoles 3, Jueves 4 y Viernes 5 de septiembre | 8:30 P.M.<br>Sábado 6 de septiembre | 5:00 P.M.<br>Miércoles 3: Foro después de la obra",
        "company": "TEATRO AVANTE | Miami, EE.UU.",
        "title": "CARRUSEL",
        "credits": "Escrita por Abel González Melo | Dirigida por Jackie Briceño<br>Elenco: Julio Rodríguez, Alina Interian, Monica Quintero, Isabella Chirinos",
        "synopsis": "En una clase de matemáticas una adolescente agrede a sus compañeros de manera violenta. Su abuelo, una maestra y una doctora que analizan la extraña conducta de la menor, abren la puerta de un pasado que revela vínculos secretos entre los cuatro que inevitablemente dictarán sus destinos en un país en reciente democracia que al parecer ha vivido un extenso período de dictadura.",
        "venue": "Westchester Cultural Arts Center | 7930 S.W. 40th Street (Tropical Park), Miami",
        "contact": "En español con supertítulos en inglés"
    },
    {
        "num": 2,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra2.png",
        "alt": "ZOMBI MANIFIESTO",
        "dates": "Miércoles 10, Jueves 11 y Viernes 12 de septiembre | 8:30 P.M.<br>Miércoles 10: Foro después de la obra",
        "company": "COMPAÑÍA ABUELA KATIUSKA, SALA VERDI y PAZO DA CULTURA DE NARÓN | Montevideo, URUGUAY / Galicia, ESPAÑA",
        "title": "ZOMBI MANIFIESTO",
        "credits": "Escrita y dirigida por Santiago Sanguinetti<br>Elenco: Paula Lieberman, Rogelio Gracia, Carmen Laguzzi, Santiago Sanguinetti",
        "synopsis": "El cadáver de un militar desaparece tras un desentierro clandestino y un secuestro. Una burócrata ejemplar reclama un entierro digno. El muerto se presenta y exige justicia. Entretanto, dos jóvenes se preguntan cuál es la mejor herramienta para cambiar el mundo, ¿la corrección política o la conciencia de clase? Zombi manifiesto está estructurada en once escenas que recuerdan que no alcanza con interpretar de diversas maneras el mundo, de lo que se trata es de transformarlo.",
        "venue": "Westchester Cultural Arts Center | 7930 S.W. 40th Street (Tropical Park), Miami",
        "contact": "En español con supertítulos en inglés"
    },
    {
        "num": 3,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra3.png",
        "alt": "HISTORIA DE UN JABALÍ (O ALGO DE RICARDO III)",
        "dates": "Jueves 11 y Viernes 12 de septiembre | 8:30 P.M.<br>Sábado 13 de septiembre | 5:00 P.M.<br>Jueves 11: Foro después de la obra",
        "company": "FUNDACIÓN TEATRO A MIL | Santiago de Chile, CHILE",
        "title": "HISTORIA DE UN JABALÍ (O ALGO DE RICARDO III)",
        "credits": "Escrita por Gabriel Calderón | Dirigida por Cristian Plana<br>Elenco: Marcelo Alonso & Francisco Reyes",
        "synopsis": "Dos actores se enfrentan al reto de interpretar a Ricardo, el monarca despiadado de la tragedia de William Shakespeare. Llevan toda la vida haciendo papeles secundarios y piensan que merecen esta oportunidad. Sin embargo, consideran que el resto del elenco no está a su altura y no les gusta nada de lo que les propone el director. Durante la construcción del personaje, las afinidades entre los actores y el monarca inglés empiezan a aflorar. Una pieza que entrega un espacio para reflexionar sobre los límites de la ambición humana, los mecanismos de poder contemporáneos, el deseo y el resentimiento.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "En español con supertítulos en inglés"
    },
    {
        "num": 4,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra4.png",
        "alt": "A FUEGO",
        "dates": "Jueves 11 y Viernes 12 de septiembre | 8:30 P.M.<br>Sábado 13 de septiembre | 5:00 P.M.<br>Viernes 12: Foro después de la obra",
        "company": "MOLA PRODUCCIONS | Cataluña, ESPAÑA",
        "title": "A FUEGO",
        "credits": "Escrita por Pablo Macho Otero | Dirigida por Emma Arquillué y Pablo Macho Otero<br>Elenco: Pablo Macho Otero",
        "synopsis": "Eróstrato, un pastor de la Antigua Grecia, incendió el templo de Artemisa de Éfeso para pasar a la posteridad. En este monólogo íntegramente en verso, lleno de sátira, juegos de palabras y metateatralidad, la fascinación del protagonista por Eróstrato se convierte progresivamente en una obsesión. Saltando de un personaje a otro, el autor-intérprete se ríe de su propia megalomanía, invitándonos a reflexionar sobre el narcisismo imperante de nuestra época y el deseo humano de dejar huella.",
        "venue": "Koubek Center Theatre | 2705 S.W. 3rd Street, Miami",
        "contact": "Monólogo en verso"
    },
    {
        "num": 5,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra5.png",
        "alt": "ODD MAN OUT (EL QUE QUEDA FUERA)",
        "dates": "Miércoles 17, Jueves 18 y Viernes 19 de septiembre | 8:30 P.M.<br>Miércoles 17: Foro después de la obra",
        "company": "PITCHBLACK | New York City, EE.UU. / Buenos Aires, ARGENTINA",
        "title": "ODD MAN OUT (EL QUE QUEDA FUERA)",
        "credits": "Creadores y directores: Carlos Armesto, Martín Bondone y Facundo Bogarín<br>Elenco: Agustina Cedraschi, Lorenza Bernasconi, Giorgia Valenti, Mauricio Marte, Facundo Bogarín, Gonzalo Trigueros, D Henry Hanson",
        "synopsis": "ODD MAN OUT es una experiencia sensorial inmersiva en completa oscuridad que despierta tus sentidos y tu imaginación. El público aborda un vuelo de PITCHBLACK Airlines y experimenta la historia de un músico ciego de Buenos Aires a través del sonido binaural 360°, el olfato, el gusto y el tacto. Una vivencia teatral transformadora galardonada como Mejor Experiencia Teatral Única de 2025 por la Off Broadway Alliance.",
        "venue": "Westchester Cultural Arts Center | 7930 S.W. 40th Street (Tropical Park), Miami",
        "contact": "Experiencia sensorial inmersiva a oscuras"
    },
    {
        "num": 6,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra6.png",
        "alt": "SUEÑO",
        "dates": "Miércoles 17, Jueves 18 y Viernes 19 de septiembre | 7:00 P.M.<br>Jueves 18: Foro después de la obra",
        "company": "COMPAÑÍA CRIOLLA y FESTIVALES DE BUENOS AIRES | Buenos Aires, ARGENTINA",
        "title": "SUEÑO",
        "credits": "Escrita y dirigida por Emiliano Dionisi (inspirada en Shakespeare)<br>Elenco: Emiliano Dionisi, Lucía Baya Casal, Tomás Castiglione, Marina Caracciolo",
        "synopsis": "Una compañía de artistas se junta en el bosque a ensayar una obra, sin advertir que el lugar está plagado de seres mágicos dispuestos a jugar con sus emociones. Inspirada en Sueño de una noche de verano de Shakespeare, cuatro intérpretes encarnan a todos los personajes en un verdadero torbellino teatral lleno de ritmo, poesía, música y humor. Ganadora del Certamen Barroco de Almagro y candidata a los Premios Max 2026.",
        "venue": "Koubek Center Theatre | 2705 S.W. 3rd Street, Miami",
        "contact": "En español"
    },
    {
        "num": 7,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra7.png",
        "alt": "PUNDONOR",
        "dates": "Jueves 18 y Viernes 19 de septiembre | 8:30 P.M.<br>Sábado 20 de septiembre | 5:00 P.M.<br>Viernes 19: Foro después de la obra",
        "company": "Buenos Aires, ARGENTINA",
        "title": "PUNDONOR",
        "credits": "Escrita por Andrea Garrote | Dirigida por Rafael Spregelburd y Andrea Garrote<br>Elenco: Andrea Garrote",
        "synopsis": "Claudia Pérez Espinosa, profesora universitaria y doctora en Sociología, vuelve a las aulas tras tomarse una licencia. Su clase de introducción a Michel Foucault se ve interrumpida constantemente por su frágil situación personal y emocional: siente la imperiosa necesidad de dar explicaciones y redimirse frente a sus alumnos. Aclamado unipersonal premiado por GETEA y nominado a los Premios María Guerrero.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "En español con supertítulos en inglés"
    },
    {
        "num": 8,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra8.png",
        "alt": "DÍA INTERNACIONAL DEL NIÑO | LAS ASOMBROSAS AVENTURAS DE ROBINSON CRUSOE",
        "dates": "Sábado 19 de septiembre | 5:00 P.M. en Key Biscayne Community Center (10 Village Green Way)<br>Domingo 20 de septiembre | 5:00 P.M. en Koubek Center Theatre (2705 SW 3rd St)<br>Actividades familiares y talleres | Entrada Gratuita",
        "company": "TEATRO SALVAJE | Miami, EE.UU.",
        "title": "DÍA INTERNACIONAL DEL NIÑO | LAS ASOMBROSAS AVENTURAS DE ROBINSON CRUSOE",
        "credits": "Escrita por Victor Hugo Cortés | Dirigida por Luciano Cortés<br>Elenco: Juan Bautista, Cote Composto",
        "synopsis": "Narra la historia de un joven audaz que tras naufragar llega a una isla desierta donde conoce personajes inolvidables. Con creatividad y optimismo, Robinson se las ingeniará para subsistir y aprenderá el valor de la amistad mientras busca la manera de volver a su hogar. Un espectáculo interactivo que conecta a grandes y chicos con la fantasía, el juego y el poder vital de la imaginación.",
        "venue": "Key Biscayne Community Center & Koubek Center Theatre",
        "contact": "Teatro infantil y familiar | Entrada Libre"
    },
    {
        "num": 9,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra9.png",
        "alt": "HAMLET",
        "dates": "Jueves 24, Viernes 25 y Sábado 26 de septiembre | 8:30 P.M.<br>Jueves 24: Foro después de la obra",
        "company": "TEATRO LA PLAZA | Lima, PERÚ",
        "title": "HAMLET",
        "credits": "Escrita por W. Shakespeare | Adaptación libre y dirección: Chela De Ferrari<br>Elenco: Octavio Bernaza, Jaime Cruz, Lucas Demarchi, Manuel García, Diana Gutiérrez, Cristina León Barandiarán, Ximena Rodríguez, Álvaro Toledo",
        "synopsis": "Un grupo de personas con síndrome de Down toma el escenario para compartir sus anhelos y frustraciones a través de una versión libre de Hamlet. La obra es un tejido entre el texto de Shakespeare y la vida de los actores, y toma como punto de partida la pregunta que nos formula frente a la existencia: ¿Ser o no ser? ¿Qué implica ser para personas que no encuentran espacios donde se los tome en cuenta? Obra internacionalmente aclamada.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "En español con supertítulos en inglés"
    }
]

plays_en = [
    {
        "num": 1,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra1.png",
        "alt": "CAROUSEL",
        "dates": "Wednesday Sept 3, Thursday Sept 4, Friday Sept 5 | 8:30 P.M.<br>Saturday Sept 6 | 5:00 P.M.<br>Wednesday Sept 3: Post-performance discussion",
        "company": "TEATRO AVANTE | Miami, USA",
        "title": "CAROUSEL",
        "credits": "Written by Abel González Melo | Directed by Jackie Briceño<br>Cast: Julio Rodríguez, Alina Interian, Monica Quintero, Isabella Chirinos",
        "synopsis": "In a mathematics class, a teenage girl violently attacks her classmates. Her grandfather, a teacher, and a doctor analyze the minor's strange behavior, opening the door to a past that reveals secret bonds among the four of them that will inevitably dictate their destinies in a recently democratic country that has apparently lived through an extended period of dictatorship.",
        "venue": "Westchester Cultural Arts Center | 7930 S.W. 40th Street (Tropical Park), Miami",
        "contact": "In Spanish with English supertitles"
    },
    {
        "num": 2,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra2.png",
        "alt": "ZOMBIE MANIFESTO",
        "dates": "Wednesday Sept 10, Thursday Sept 11, Friday Sept 12 | 8:30 P.M.<br>Wednesday Sept 10: Post-performance discussion",
        "company": "COMPAÑÍA ABUELA KATIUSKA, SALA VERDI & PAZO DA CULTURA DE NARÓN | Montevideo, URUGUAY / Galicia, SPAIN",
        "title": "ZOMBIE MANIFESTO",
        "credits": "Written and directed by Santiago Sanguinetti<br>Cast: Paula Lieberman, Rogelio Gracia, Carmen Laguzzi, Santiago Sanguinetti",
        "synopsis": "The corpse of a military officer vanishes following a clandestine exhumation and abduction. An exemplary bureaucrat demands a dignified burial. The deceased appears and demands justice. Meanwhile, two young people wonder what the best tool for changing the world is: political correctness or class consciousness? Zombie Manifesto is structured in eleven scenes that serve as a reminder that it is not enough to interpret the world in various ways; the point is to transform it.",
        "venue": "Westchester Cultural Arts Center | 7930 S.W. 40th Street (Tropical Park), Miami",
        "contact": "In Spanish with English supertitles"
    },
    {
        "num": 3,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra3.png",
        "alt": "STORY OF A BOAR (OR SOMETHING ABOUT RICHARD III)",
        "dates": "Thursday Sept 11, Friday Sept 12 | 8:30 P.M.<br>Saturday Sept 13 | 5:00 P.M.<br>Thursday Sept 11: Post-performance discussion",
        "company": "TEATRO A MIL FOUNDATION | Santiago, CHILE",
        "title": "STORY OF A BOAR (OR SOMETHING ABOUT RICHARD III)",
        "credits": "Written by Gabriel Calderón | Directed by Cristian Plana<br>Cast: Marcelo Alonso & Francisco Reyes",
        "synopsis": "Two actors face the challenge of playing Richard, the ruthless monarch of William Shakespeare's tragedy. They have spent their entire lives in supporting roles and believe they deserve this opportunity. During character construction, affinities between the actors and the English monarch begin to surface. A piece delivering a vital space to reflect on the limits of human ambition, contemporary mechanisms of power, desire, and resentment.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "In Spanish with English supertitles"
    },
    {
        "num": 4,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra4.png",
        "alt": "ON FIRE (A FUEGO)",
        "dates": "Thursday Sept 11, Friday Sept 12 | 8:30 P.M.<br>Saturday Sept 13 | 5:00 P.M.<br>Friday Sept 12: Post-performance discussion",
        "company": "MOLA PRODUCCIONS | Catalonia, SPAIN",
        "title": "ON FIRE (A FUEGO)",
        "credits": "Written by Pablo Macho Otero | Directed by Emma Arquillué & Pablo Macho Otero<br>Cast: Pablo Macho Otero",
        "synopsis": "Erostratus, a shepherd from Ancient Greece, set fire to the Temple of Artemis at Ephesus to go down in posterity. In this monologue entirely in verse, full of satire, wordplay, and metatheatre, the protagonist's fascination with Erostratus becomes an obsession. Jumping from character to character, the performer laughs at his own megalomania, inviting us to reflect on contemporary narcissism and the human desire to leave a mark.",
        "venue": "Koubek Center Theatre | 2705 S.W. 3rd Street, Miami",
        "contact": "Verse monologue in Spanish"
    },
    {
        "num": 5,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra5.png",
        "alt": "ODD MAN OUT",
        "dates": "Wednesday Sept 17, Thursday Sept 18, Friday Sept 19 | 8:30 P.M.<br>Wednesday Sept 17: Post-performance discussion",
        "company": "PITCHBLACK | New York City, USA / Buenos Aires, ARGENTINA",
        "title": "ODD MAN OUT",
        "credits": "Created and directed by Carlos Armesto, Martín Bondone & Facundo Bogarín<br>Cast: Agustina Cedraschi, Lorenza Bernasconi, Giorgia Valenti, Mauricio Marte, Facundo Bogarín, Gonzalo Trigueros, D Henry Hanson",
        "synopsis": "ODD MAN OUT is an immersive sensory experience in complete darkness that awakens your senses and imagination. The audience boards a PITCHBLACK Airlines flight and experiences the journey of a blind musician from Buenos Aires through 360° binaural sound, smell, taste, and touch. A transformative theatrical journey named Best Unique Theatrical Experience of 2025 by the Off Broadway Alliance.",
        "venue": "Westchester Cultural Arts Center | 7930 S.W. 40th Street (Tropical Park), Miami",
        "contact": "Immersive sensory experience in total darkness"
    },
    {
        "num": 6,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra6.png",
        "alt": "DREAM (SUEÑO)",
        "dates": "Wednesday Sept 17, Thursday Sept 18, Friday Sept 19 | 7:00 P.M.<br>Thursday Sept 18: Post-performance discussion",
        "company": "COMPAÑÍA CRIOLLA & BUENOS AIRES FESTIVALS | Buenos Aires, ARGENTINA",
        "title": "DREAM (SUEÑO)",
        "credits": "Written and directed by Emiliano Dionisi (inspired by Shakespeare)<br>Cast: Emiliano Dionisi, Lucía Baya Casal, Tomás Castiglione, Marina Caracciolo",
        "synopsis": "A theater troupe gathers in the woods to rehearse a play, unaware that magical creatures are ready to play whimsically with their emotions. Inspired by Shakespeare's A Midsummer Night's Dream, four performers embody all the characters in a theatrical whirlwind of rhythm, physical deployment, poetry, and humor. Winner of the Almagro Baroque Competition and nominated for the Max Awards 2026.",
        "venue": "Koubek Center Theatre | 2705 S.W. 3rd Street, Miami",
        "contact": "In Spanish"
    },
    {
        "num": 7,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra7.png",
        "alt": "PUNDONOR",
        "dates": "Thursday Sept 18, Friday Sept 19 | 8:30 P.M.<br>Saturday Sept 20 | 5:00 P.M.<br>Friday Sept 19: Post-performance discussion",
        "company": "Buenos Aires, ARGENTINA",
        "title": "PUNDONOR",
        "credits": "Written by Andrea Garrote | Directed by Rafael Spregelburd & Andrea Garrote<br>Cast: Andrea Garrote",
        "synopsis": "Claudia Pérez Espinosa, university professor and Doctor of Sociology, returns to the classroom after taking leave. Her introductory lecture on Michel Foucault is repeatedly interrupted by her own fragile emotional state: she feels an urgent need to explain herself and seek redemption before her students. Acclaimed solo performance honored by GETEA and nominated for the María Guerrero Awards.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "In Spanish with English supertitles"
    },
    {
        "num": 8,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra8.png",
        "alt": "INTERNATIONAL CHILDREN'S DAY | THE AMAZING ADVENTURES OF ROBINSON CRUSOE",
        "dates": "Saturday Sept 19 | 5:00 P.M. at Key Biscayne Community Center (10 Village Green Way)<br>Sunday Sept 20 | 5:00 P.M. at Koubek Center Theatre (2705 SW 3rd St)<br>Family activities and workshops | Free Admission",
        "company": "TEATRO SALVAJE | Miami, USA",
        "title": "INTERNATIONAL CHILDREN'S DAY | THE AMAZING ADVENTURES OF ROBINSON CRUSOE",
        "credits": "Written by Victor Hugo Cortés | Directed by Luciano Cortés<br>Cast: Juan Bautista, Cote Composto",
        "synopsis": "Tells the story of a daring young man who, after being shipwrecked, arrives on a deserted island where he meets unforgettable characters. With creativity and optimism, Robinson finds ingenious ways to survive and learns the true value of friendship. An interactive show connecting audiences of all ages with fantasy, adventure, and the vital power of imagination.",
        "venue": "Key Biscayne Community Center & Koubek Center Theatre",
        "contact": "Children and family theater | Free Admission"
    },
    {
        "num": 9,
        "img": "../../../assets/Fotos_Archivos/Edicion_40/cropped/Obra9.png",
        "alt": "HAMLET",
        "dates": "Thursday Sept 24, Friday Sept 25, Saturday Sept 26 | 8:30 P.M.<br>Thursday Sept 24: Post-performance discussion",
        "company": "TEATRO LA PLAZA | Lima, PERU",
        "title": "HAMLET",
        "credits": "Written by W. Shakespeare | Free adaptation and directed by Chela De Ferrari<br>Cast: Octavio Bernaza, Jaime Cruz, Lucas Demarchi, Manuel García, Diana Gutiérrez, Cristina León Barandiarán, Ximena Rodríguez, Álvaro Toledo",
        "synopsis": "A group of actors with Down syndrome takes the stage to share their hopes and frustrations through a free adaptation of Hamlet. The production weaves Shakespeare's classic text with the performers' own lives, revolving around existence's fundamental question: To be or not to be? What does it mean to exist for people who fight for recognition? Internationally acclaimed production.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "In Spanish with English supertitles"
    }
]

plays_html_es = "\n".join([build_play_article(**p) for p in plays_es])
plays_html_en = "\n".join([build_play_article(**p) for p in plays_en])

full_html_es = get_template("es", 2026, 40, plays_html_es)
full_html_en = get_template("en", 2026, 40, plays_html_en)

es_dir = os.path.join(workspace, "es", "archivos-del-festival", "2026")
en_dir = os.path.join(workspace, "en", "archivos-del-festival", "2026")

os.makedirs(es_dir, exist_ok=True)
os.makedirs(en_dir, exist_ok=True)

es_file = os.path.join(es_dir, "index.html")
en_file = os.path.join(en_dir, "index.html")

with open(es_file, "w", encoding="utf-8") as f:
    f.write(full_html_es)

with open(en_file, "w", encoding="utf-8") as f:
    f.write(full_html_en)

print("Generated:", es_file)
print("Generated:", en_file)
