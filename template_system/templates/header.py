HEADER = """<!doctype html>
<html lang="en">
<head>
    <title>Zodiac - {}</title>
    <meta charset="utf-8">
    <meta name="author" content="Zødiac">
    <meta name="description" content="Personal website">
    <meta name="keywords" content="Blender, DIY, Zødiac, Zodiac, ZodiacFRA">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>◾</text></svg>">
    <link rel="stylesheet" href="{}/style.css">
</head>

<body>
    <header>
        <div style="margin-right: 100px;">
            <h1><a href='{}/index.html'>Zødiac</a></h1>
            <h3 style='margin-top: -16px'>Code & 3d art</h3>
        </div>
        <div class="header_icons">
          <a href="{}/3d.html" class="header_block">
            <img class="header_icon" style="height: auto; width: 33px; margin-top: 9px;" src="./images/misc/layers-svgrepo-com.svg">
            <h2 class="header_link">3D</h2>
          </a>
          <a href="{}/code.html" class="header_block">
            <img class="header_icon" style="height: auto; width: 44px; margin-top: 12px;" src="./images/misc/keyboard-svgrepo-com.svg">
            <h2 class="header_link">Code</h2>
          </a>
          <a href="https://github.com/ZodiacFRA" class="header_block">
            <img class="header_icon" style="height: auto; width: 36px; margin-top: 10px;" src="./images/misc/github-svgrepo-com.svg">
            <h2 class="header_link">Github</h2>
          </a>
          <a href="{}/contact.html" class="header_block">
            <img class="header_icon" style="height: auto; width: 40px; margin-top: 12px;" src="./images/misc/email-svgrepo-com.svg">
            <h2 class="header_link">Contact</h2>
          </a>

        </div>
    </header>
<!--------------------------------------------------------------------------- HEADER END -->"""


OLD_HEADER = """<!doctype html>
<html lang="en">
<head>
    <title>Zodiac - {}</title>
    <meta charset="utf-8">
    <meta name="author" content="Zødiac">
    <meta name="description" content="Personal website">
    <meta name="keywords" content="Blender, DIY, Zødiac, Zodiac, ZodiacFRA">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>◾</text></svg>">
    <link rel="stylesheet" href="{}/style.css">
</head>

<body>
    <header>
        <div style="margin-right: 100px;">
            <h1><a href='{}/index.html'>Zødiac</a></h1>
            <h3 style='margin-top: -16px'>Code & 3d art</h3>
        </div>
        <div class="header_icons">
            <a href='https://github.com/ZodiacFRA'>
                <img class="header_icon" src="{}/images/misc/github.svg">
            </a>
            <a href="{}/contact.html">
                <img class="header_icon" src="{}/images/misc/email.svg">
            </a>
        </div>
    </header>
<!--------------------------------------------------------------------------- HEADER END -->"""
