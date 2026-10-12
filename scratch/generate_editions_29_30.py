import os

workspace = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF-Miami\IHTF"

def get_template(lang, year, roman, tribute_target, plays_html):
    if lang == "es":
        title = f"{roman} Festival Internacional de Teatro Hispano de Miami ({year}) | Archivos"
        desc = f"Programa oficial de obras presentadas en la {year[-2:] if year=='2014' or year=='2015' else year}ª edición del Festival Internacional de Teatro Hispano de Miami ({year}) - Homenaje a {tribute_target}."
        canonical = f"https://vayol-art.github.io/IHTF/es/archivos-del-festival/{year}/"
        en_switch_url = f"../../../en/archivos-del-festival/{year}/"
        header_h2 = f"{roman} FESTIVAL INTERNACIONAL DE TEATRO HISPANO DE MIAMI | HOMENAJE A {tribute_target.upper()}"
        header_p = f"PROGRAMA {year}"
        hero_title = "ARCHIVOS DEL FESTIVAL"
        program_label = "PROGRAMA"
        contact_label = "CONTÁCTANOS"
        about_label = "SOBRE NOSOTROS"
        inscrip_label = "INSCRIPCIONES 41° FESTIVAL"
        newsletter_h2 = "Suscríbete a nuestro Newsletter"
        newsletter_p = "Recibe información actualizada sobre el IHTF"
        privacy_label = "Políticas de privacidad"
        terms_label = "Términos y condiciones"
        
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
        
        home_href = "../../#inicio"
        about_href_1 = "../../nosotros/#compania"
        about_href_2 = "../../nosotros/#personal"
        current_lang_text = "Español"
        
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

        newsletter_h2 = "Subscribe to our Newsletter"
        newsletter_p = "Receive updated information about IHTF"
        privacy_label = "Privacy Policy"
        terms_label = "Terms & Conditions"
        home_href = "../../#inicio"

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

def format_play_article(num, ed_num, img_alt, dates, company, title, credits, synopsis, venue, contact):
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

print("Template generator function defined.")
