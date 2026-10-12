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
    return f'''        <!-- Obra {num} -->
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
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra1.png",
        "alt": "LAS DELICADAS LÁGRIMAS DE LA LUNA MENGUANTE",
        "dates": "Jueves 4, Viernes 5 y Sábado 6 de septiembre | 8:30 P.M.<br>Jueves 4: Foro después de la obra",
        "company": "WATER PEOPLE THEATER | VENEZUELA / Chicago - USA",
        "title": "LAS DELICADAS LÁGRIMAS DE LA LUNA MENGUANTE",
        "credits": "Escrita por Rebeca Alemán | Dirigida por Iraida Tapias<br>Elenco: Rebeca Alemán - Gabriel Porras | Voces: Laura Crotte, Anabel Sofía Ybarra y Miguel Núñez",
        "synopsis": "Inspirada en hechos reales, Las delicadas lágrimas de la luna menguante explora las continuas violaciones a los derechos humanos que enfrentan los periodistas por decir la verdad. Paulina, una periodista comprometida y defensora de las víctimas de feminicidio y de las comunidades indígenas, despierta de un coma de cuatro meses tras un brutal ataque. Para lograr justicia, debe recuperar su memoria y revelar la verdad.",
        "venue": "Westchester Cultural Arts Center | 7930 S.W. 40th Street (Tropical Park), Miami",
        "contact": "En español con supertítulos en inglés"
    },
    {
        "num": 2,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra2.png",
        "alt": "VIENTO BLANCO",
        "dates": "Viernes 5 y Sábado 6 de septiembre | 8:30 P.M.<br>Domingo 7 de septiembre | 5:00 P.M.<br>Viernes 5: Foro después de la obra",
        "company": "COMPAÑÍA TEATRO FUTURO | Buenos Aires, ARGENTINA",
        "title": "VIENTO BLANCO",
        "credits": "Escrita por Santiago Loza | Dirigida por Valeria Lois y Juanse Rausch<br>Elenco: Mariano Saborido",
        "synopsis": "Mario mantiene con su madre un hostal en un recóndito pueblo del sur. Más allá hubo un puerto que dejó de funcionar. Viajantes, marineros, gente de paso. En otra época Mario supo tener un amigo. Hay un regreso, una despedida y el deseo de Mario de huir para siempre. Entre el mar helado, ardores, cánticos y mucho viento. Viento Blanco es una suerte de invocación en cuyo recorrido hay erotismo clerical, chinos, animales de mar frío, algo de humor y también una tenue melancolía.",
        "venue": "Koubek Center Theatre | 2705 SW 3rd Street, Miami",
        "contact": "Monólogo dramático"
    },
    {
        "num": 3,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra3.png",
        "alt": "EL BROTE",
        "dates": "Jueves 11, Viernes 12 y Sábado 13 de septiembre | 8:30 P.M.<br>Jueves 11: Foro después de la obra",
        "company": "COMPAÑÍA CRIOLLA | Buenos Aires, ARGENTINA",
        "title": "EL BROTE",
        "credits": "Escrita y dirigida por Emiliano Dionisi<br>Elenco: Roberto Peloni",
        "synopsis": "A un actor se le comienzan a desdibujar los límites entre la ficción y la realidad y ahora desconfía de quien escribe los acontecimientos de su vida ¿Qué clase de personaje somos en esta historia? El nuevo espectáculo de la Compañía Criolla fue estrenado el 13 de febrero de 2023 en el Teatro del Pueblo de la Ciudad de Buenos Aires, Argentina, con una gran recepción por parte de la crítica y el público que le ha valido un reconocimiento nacional e internacional.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "En español con supertítulos en inglés"
    },
    {
        "num": 4,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra4.png",
        "alt": "LOS QUE SOBRAN",
        "dates": "Viernes 12 y Sábado 13 de septiembre | 8:30 P.M.<br>Domingo 14 de septiembre | 5:00 P.M.<br>Sábado 13: Foro después de la obra",
        "company": "LOS TRISTES TIGRES | Ciudad de México, MÉXICO",
        "title": "LOS QUE SOBRAN",
        "credits": "Escrita y dirigida por Adrián Vázquez<br>Elenco: Fátima Favela - Quetzalli Cortes - Lariza Juárez - Paula Zepeda - Mónica Vega - Iván Carbajal",
        "synopsis": "Alejandro es un tipo poco común, padece un trastorno de inestabilidad emocional; por lo tanto prefiere no meterse en problemas. Sofía, su hermana, es la líder del grupo. Edith es buena para las peleas y defiende a sus amigos. Emilio es un desmadre, en resumen. Y Camila es como la mascota del grupo, la intelectual. Los que sobran es la historia de estos cinco jóvenes que se hicieron amigos en la adolescencia, y el tiempo y las experiencias los volvieron compañeros de vida. Contada desde los ojos de una persona, es una historia de amistad, juventud, humor, rebeldía, coraje, pasión, violencia, crueldad, supervivencia y amor.",
        "venue": "Westchester Cultural Arts Center | 7930 S.W. 40th Street (Tropical Park), Miami",
        "contact": "Drama juvenil"
    },
    {
        "num": 5,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra5.png",
        "alt": "PALABODA",
        "dates": "Viernes 12 y Sábado 13 de septiembre | 8:30 P.M.<br>Domingo 14 de septiembre | 5:00 P.M.<br>Viernes 12: Foro después de la obra",
        "company": "LA TIRANA PRODUCCIONES | Cádiz, ESPAÑA",
        "title": "PALABODA",
        "credits": "Escrita por La Tirana, Rocío Sepúlveda y Juan Sebastián Domínguez | Dirigida por La Tirana<br>Elenco: Susana Rosado - Jay García",
        "synopsis": "Divertida comedia en la que se cuenta la entrañable historia de Begoñita y Juanmanué, quienes tendrán que ponerse de acuerdo para la ansiada boda que tanto espera ella y de la que tanto huye él. Ella quiere una boda como Dios manda; él no quiere ponerse zapatos porque le aprietan; ella lleva velo porque la estiliza; él no quiere anillo porque se le hinchan los dedos; ella quiere convite con tarta, baile y champán; él quiere que termine pronto para irse a pescar... PALABODA es un divertimento, un rato de risas garantizadas.",
        "venue": "Koubek Center Theatre | 2705 SW 3rd Street, Miami",
        "contact": "Comedia"
    },
    {
        "num": 6,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra6.png",
        "alt": "MAGALLANES",
        "dates": "Viernes 19 y Sábado 20 de septiembre | 8:30 P.M.<br>Domingo 21 de septiembre | 5:00 P.M.<br>Viernes 19: Foro después de la obra",
        "company": "TRYO TEATRO BANDA | Santiago de Chile, CHILE",
        "title": "MAGALLANES",
        "credits": "Escrita por Francisco Sánchez y Tryo Teatro Banda | Dirigida por Francisco Sánchez y Eduardo Irrazábal<br>Elenco: Alfredo Becerra - Javier Bolívar - Diego Chamorro - Martín Feuerhake - Daniella Rivera - Francisco Sánchez",
        "synopsis": "El portugués Fernão Magalhães lidera una expedición española que pretende llegar a las Islas de las Especias en el Asia-Pacífico navegando hacia el poniente, para lo cual debe encontrar un paso a través del continente americano hacia un nuevo océano: el Estrecho de Magallanes. Desconfianzas, traiciones, peligros, mitologías fantásticas y terroríficas, hambre, naufragios, deserciones, combates y rebeldía conspiran contra la expedición. Tryo Teatro Banda, recordando a los antiguos juglares con violín, tiple, acordeón, bajo eléctrico y percusión, nos cuenta esta historia apasionante que incluye el primer encuentro entre navegantes extranjeros y los habitantes australes de Chile.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "En español con supertítulos en inglés"
    },
    {
        "num": 7,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra7.png",
        "alt": "PROTOCOLO",
        "dates": "Viernes 19 y Sábado 20 de septiembre | 8:30 P.M.<br>Domingo 21 de septiembre | 5:00 P.M.<br>Sábado 20: Foro después de la obra",
        "company": "LA BELLO CH TEATRO | Madrid, ESPAÑA",
        "title": "PROTOCOLO",
        "credits": "Escrita y dirigida por Abel González Melo<br>Elenco: Beatriz Argüello - Ernesto Arias",
        "synopsis": "Una pareja atravesada por un conflicto ético, medioambiental, económico y político. Un estremecedor mapa humano donde el deber cívico choca con la intimidad. Una emocionante experiencia escénica protagonizada por dos primeras figuras del teatro español.",
        "venue": "Westchester Cultural Arts Center | 7930 S.W. 40th Street (Tropical Park), Miami",
        "contact": "Drama contemporáneo"
    },
    {
        "num": 8,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra8.png",
        "alt": "DÍA INTERNACIONAL DEL NIÑO - COMICÓPICOS",
        "dates": "Sábado 20 de septiembre | 5:00 P.M. en Key Biscayne Community Center (10 Village Green Way)<br>Domingo 21 de septiembre | 3:00 P.M. y 5:00 P.M. en Koubek Center Theatre (2705 SW 3rd St)<br>Actividades familiares y talleres desde las 2:00 P.M. | Entrada Gratuita",
        "company": "COMPAÑÍA FUGAZ | Buenos Aires, ARGENTINA",
        "title": "DÍA INTERNACIONAL DEL NIÑO | COMICÓPICOS",
        "credits": "Creada y dirigida por Osqui Guzmán y Leticia González de Lellis<br>Elenco: Leticia González de Lellis - Osqui Guzmán",
        "synopsis": "Comicópicos son dos divertidos artistas de variedades. A partir de juegos, escenas y canciones, sacan de la galera historias disparatadas, momentos cómicos y de interacción con el público de todas las edades. Brillo, talento y emoción garantizadas. Los Comicópicos dicen: “nuestras actuaciones son como la vida misma, no tienen guión escrito”. Una divertida experiencia de impro para toda la familia.",
        "venue": "Key Biscayne Community Center & Koubek Center Theatre | Miami",
        "contact": "Espectáculo familiar interactivo | Entrada Gratuita"
    },
    {
        "num": 9,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra9.png",
        "alt": "LEAR / UMPA! La Voz Presente",
        "dates": "Jueves 25, Viernes 26 y Sábado 27 de septiembre | 8:30 P.M.<br>Domingo 28 de septiembre | 5:00 P.M.<br>Viernes 26: Foro después de la obra",
        "company": "TEATRO AVANTE | Miami, U.S.A.",
        "title": "LEAR / UMPA! La Voz Presente",
        "credits": "Inspirada en “El Rey Lear” de William Shakespeare | Escrita y dirigida por Neher Jacqueline Briceño<br>Elenco LEAR: Julio Rodríguez - Claudia Valdés - Claudia Tomás - Laura Alemán - Daniel Romero",
        "synopsis": "La caída del poder patriarcal a través de un viaje fragmentado por la memoria del Rey Lear es la premisa que sostiene esta perspectiva contemporánea del clásico Shakespeariano, donde las confrontaciones internas padre/hijas y las consecuencias del poder toman la palabra. Entre ellos el Bufón, puente que irrumpe con verdades que ya no pueden callarse porque en Lear el tiempo no avanza, se repite y se abre como una herida.<br><br><strong>UMPA! La Voz Presente | Homenaje a Mario Ernesto Sánchez</strong><br><em>Elenco: Alina Interián, Marilyn Romero, Gerardo Riverón, Yani Martín</em><br>Evocación escénica con actores de Teatro Avante para revivir instantes que fueron posibles gracias a la dirección artística y producción de Mario Ernesto Sánchez, fundador de la compañía y creador del Festival Internacional de Teatro Hispano de Miami. Dos grandes proyectos que trascendieron fronteras, sostenidos por su mirada amplia y su ímpetu incansable por defender las artes escénicas. ¡Hoy y siempre, su voz e impulso resuenan sobre la escena!",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "En español con supertítulos en inglés"
    }
]

plays_en = [
    {
        "num": 1,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra1.png",
        "alt": "LAS DELICADAS LÁGRIMAS DE LA LUNA MENGUANTE (The Delicate Tears of the Waning Moon)",
        "dates": "Thursday, Friday & Saturday; September 4, 5 & 6 | 8:30 pm<br>Thursday, September 4: Forum after the performance",
        "company": "WATER PEOPLE THEATER | Venezuela / Chicago - USA",
        "title": "LAS DELICADAS LÁGRIMAS DE LA LUNA MENGUANTE (The Delicate Tears of the Waning Moon)",
        "credits": "Written by Rebeca Alemán | Directed by Iraida Tapias<br>Cast: Rebeca Alemán - Gabriel Porras | Voices: Laura Crotte, Anabel Sofía Ybarra, and Miguel Núñez",
        "synopsis": "Inspired by true events, The Delicate Tears of the Waning Moon explores the ongoing human rights violations faced by journalists for speaking the truth. Paulina, a committed journalist and advocate for victims of femicide and indigenous communities, awakens from a four-month coma following a brutal attack. To achieve justice, she must reclaim her memory and reveal the truth.",
        "venue": "Westchester Cultural Arts Center | 7930 S.W. 40th Street (Tropical Park), Miami",
        "contact": "In Spanish with English supertitles"
    },
    {
        "num": 2,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra2.png",
        "alt": "VIENTO BLANCO (White Wind)",
        "dates": "Friday & Saturday, September 5 & 6 | 8:30 pm<br>Sunday, September 7 | 5:00 pm<br>Friday, September 5: Forum after the performance",
        "company": "COMPAÑÍA TEATRO FUTURO | Buenos Aires, Argentina",
        "title": "VIENTO BLANCO (White Wind)",
        "credits": "Written by Santiago Loza | Directed by Valeria Lois & Juanse Rausch<br>Cast: Mariano Saborido",
        "synopsis": "Mario runs an inn with his mother in a remote southern outpost. Beyond it lies a forgotten port that long ago ceased operating. Transient sailors, travelers, passing souls. Once, Mario had a friend. There is a return, a parting farewell, and Mario's yearning to escape forever. Amidst the icy sea, fierce passions, sacred chants, and howling wind. Viento Blanco is an evocative journey where clerical eroticism, Chinese merchants, arctic marine life, humor, and tender melancholy converge.",
        "venue": "Koubek Center Theatre | 2705 SW 3rd Street, Miami",
        "contact": "Dramatic monologue"
    },
    {
        "num": 3,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra3.png",
        "alt": "EL BROTE (The Outbreak)",
        "dates": "Thursday, Friday & Saturday; September 11, 12 & 13 | 8:30 pm<br>Thursday, September 11: Forum after the performance",
        "company": "COMPAÑÍA CRIOLLA | Buenos Aires, Argentina",
        "title": "EL BROTE (The Outbreak)",
        "credits": "Written & Directed by Emiliano Dionisi<br>Cast: Roberto Peloni",
        "synopsis": "For an actor, the boundaries between fiction and reality begin to dissolve, and he now mistrusts whoever is scripting the events of his life. What kind of character are we in this story? Premiered in February 2023 at Teatro del Pueblo in Buenos Aires, this acclaimed production by Compañía Criolla achieved widespread critical and public acclaim, winning major national and international awards.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "In Spanish with English supertitles"
    },
    {
        "num": 4,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra4.png",
        "alt": "LOS QUE SOBRAN (Those Left Over)",
        "dates": "Friday & Saturday, September 12 & 13 | 8:30 pm<br>Sunday, September 14 | 5:00 pm<br>Saturday, September 13: Forum after the performance",
        "company": "LOS TRISTES TIGRES | Mexico City, Mexico",
        "title": "LOS QUE SOBRAN (Those Left Over)",
        "credits": "Written & Directed by Adrián Vázquez<br>Cast: Fátima Favela - Quetzalli Cortes - Lariza Juárez - Paula Zepeda - Mónica Vega - Iván Carbajal",
        "synopsis": "Alejandro is unusual; suffering from emotional instability, he prefers to avoid trouble. Sofía, his sister, leads the pack. Edith is a fierce fighter who defends her friends. Emilio is pure chaos. And Camila is the intellectual mascot. Los que sobran tells the story of these five youths who forged an unbreakable bond in adolescence, tempered into lifelong companions by time and adversity. Told through a singular perspective, it is a visceral story of friendship, youth, defiance, passion, violence, survival, and love.",
        "venue": "Westchester Cultural Arts Center | 7930 S.W. 40th Street (Tropical Park), Miami",
        "contact": "Youth drama"
    },
    {
        "num": 5,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra5.png",
        "alt": "PALABODA (The Wedding)",
        "dates": "Friday & Saturday, September 12 & 13 | 8:30 pm<br>Sunday, September 14 | 5:00 pm<br>Friday, September 12: Forum after the performance",
        "company": "LA TIRANA PRODUCCIONES | Cádiz, Spain",
        "title": "PALABODA (The Wedding)",
        "credits": "Written by La Tirana, Rocío Sepúlveda & Juan Sebastián Domínguez | Directed by La Tirana<br>Cast: Susana Rosado - Jay García",
        "synopsis": "A hilarious comedy recounting the heartwarming story of Begoñita and Juanmanué, who must come to terms over the coveted wedding she eagerly anticipates and he desperately avoids. She wants a grand traditional ceremony; he hates tight shoes; she wears a veil to look slender; he rejects rings because his fingers swell; she dreams of a banquet with cake, dancing, and champagne; he just wants it over quickly so he can go fishing... PALABODA is pure delight and guaranteed laughs.",
        "venue": "Koubek Center Theatre | 2705 SW 3rd Street, Miami",
        "contact": "Comedy"
    },
    {
        "num": 6,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra6.png",
        "alt": "MAGALLANES (Magellan)",
        "dates": "Friday & Saturday, September 19 & 20 | 8:30 pm<br>Sunday, September 21 | 5:00 pm<br>Friday, September 19: Forum after the performance",
        "company": "TRYO TEATRO BANDA | Santiago, Chile",
        "title": "MAGALLANES (Magellan)",
        "credits": "Written by Francisco Sánchez & Tryo Teatro Banda | Directed by Francisco Sánchez & Eduardo Irrazábal<br>Cast: Alfredo Becerra - Javier Bolívar - Diego Chamorro - Martín Feuerhake - Daniella Rivera - Francisco Sánchez",
        "synopsis": "Portuguese navigator Fernão de Magalhães leads a Spanish fleet seeking to reach the Spice Islands of Asia-Pacific by sailing west, searching for an elusive route through the Americas to a new ocean: what would become known as the Strait of Magellan. Mistrust, treachery, perils, mythical beasts, starvation, shipwreck, mutiny, and rebellion threaten the voyage. Evoking medieval jugglers with violin, tiple, accordion, electric bass, and percussion, Tryo Teatro Banda narrates this breathtaking epic, capturing the first encounter between European explorers and the indigenous peoples of southern Chile.",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "In Spanish with English supertitles"
    },
    {
        "num": 7,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra7.png",
        "alt": "PROTOCOLO (Protocol)",
        "dates": "Friday & Saturday, September 19 & 20 | 8:30 pm<br>Sunday, September 21 | 5:00 pm<br>Saturday, September 20: Forum after the performance",
        "company": "LA BELLO CH TEATRO | Madrid, Spain",
        "title": "PROTOCOLO (Protocol)",
        "credits": "Written & Directed by Abel González Melo<br>Cast: Beatriz Argüello - Ernesto Arias",
        "synopsis": "A couple caught in an ethical, environmental, economic, and political crisis. A gripping human landscape where civic duty clashes with personal intimacy. A thrilling theatrical experience starring two leading lights of contemporary Spanish theatre.",
        "venue": "Westchester Cultural Arts Center | 7930 S.W. 40th Street (Tropical Park), Miami",
        "contact": "Contemporary drama"
    },
    {
        "num": 8,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra8.png",
        "alt": "INTERNATIONAL CHILDREN'S DAY - COMICÓPICOS",
        "dates": "Saturday, September 20 | 5:00 pm at Key Biscayne Community Center (10 Village Green Way)<br>Sunday, September 21 | 3:00 pm & 5:00 pm at Koubek Center Theatre (2705 SW 3rd St)<br>Family activities and workshops starting at 2:00 pm | Free Admission",
        "company": "COMPAÑÍA FUGAZ | Buenos Aires, Argentina",
        "title": "INTERNATIONAL CHILDREN'S DAY | COMICÓPICOS",
        "credits": "Created & Directed by Osqui Guzmán & Leticia González de Lellis<br>Cast: Leticia González de Lellis - Osqui Guzmán",
        "synopsis": "Comicópicos are two charismatic variety artists who pull hilarious stories, comedic sketches, and games out of their hat for audiences of all ages. Brilliance, talent, and emotion guaranteed! As the Comicópicos say: 'Our shows are like life itself—they have no written script!' A delightful improvisational theatre experience for the whole family.",
        "venue": "Key Biscayne Community Center & Koubek Center Theatre | Miami",
        "contact": "Interactive family show | Free admission"
    },
    {
        "num": 9,
        "img": "../../../assets/Fotos_Archivos/Edicion_39/cropped/Obra9.png",
        "alt": "LEAR / UMPA! The Living Voice",
        "dates": "Thursday, Friday & Saturday; September 25, 26 & 27 | 8:30 pm<br>Sunday, September 28 | 5:00 pm<br>Friday, September 26: Forum after the performance",
        "company": "TEATRO AVANTE | Miami, U.S.A.",
        "title": "LEAR / UMPA! The Living Voice",
        "credits": "Inspired by William Shakespeare's “King Lear” | Written & Directed by Neher Jacqueline Briceño<br>LEAR Cast: Julio Rodríguez - Claudia Valdés - Claudia Tomás - Laura Alemán - Daniel Romero",
        "synopsis": "The crumbling of patriarchal power through a fractured journey across King Lear's memory underpins this contemporary take on Shakespeare's tragedy, where father-daughter confrontations and the price of power take center stage. Among them, the Fool becomes the essential bridge uttering truths that can no longer remain hidden.<br><br><strong>UMPA! The Living Voice | Tribute to Mario Ernesto Sánchez</strong><br><em>Cast: Alina Interián, Marilyn Romero, Gerardo Riverón, Yani Martín</em><br>A scenic celebration featuring Teatro Avante actors honoring the artistic vision and leadership of Mario Ernesto Sánchez, founder of the company and creator of the International Hispanic Theatre Festival of Miami. Two major cultural projects that crossed borders, driven by his tireless passion to champion the performing arts for our community. Today his voice is not history—it is momentum, rhythm, and enduring presence!",
        "venue": "Carnival Studio Theater, Adrienne Arsht Center | 1300 Biscayne Boulevard, Miami",
        "contact": "In Spanish with English supertitles"
    }
]

html_blocks_es = "\n\n".join([build_play_article(**p) for p in plays_es])
html_blocks_en = "\n\n".join([build_play_article(**p) for p in plays_en])

full_page_es = get_template("es", 2025, 39, html_blocks_es)
full_page_en = get_template("en", 2025, 39, html_blocks_en)

es_file = os.path.join(workspace, "es", "archivos-del-festival", "2025", "index.html")
en_file = os.path.join(workspace, "en", "archivos-del-festival", "2025", "index.html")

with open(es_file, "w", encoding="utf-8") as f:
    f.write(full_page_es)
print("Saved Spanish page:", es_file)

with open(en_file, "w", encoding="utf-8") as f:
    f.write(full_page_en)
print("Saved English page:", en_file)
