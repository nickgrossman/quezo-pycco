header = """\
<!-- fly bar -->
<div id="flybar">
<a id="nav-logo" href="{{indexpath}}">{{{ project_name }}} Documentation</a>

<div class="flybar-language">
  <div class="dropdown">
    <a id="pages-dropdown" class="flybar-button">Files
      <b class="caret"></b>
    </a>
    <ul class="dropdown-menu">
      {{#files}}
      <li><a href="{{html_file_name}}">{{filename}}</a></li>
      {{/files}}
    </ul>
  </div>
</div>
</div>
<!-- end of fly bar -->
"""

page_html = """\
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="content-type" content="text/html;charset=utf-8">
  <title>{{ title }}</title>
  <link rel="stylesheet" href="{{ stylesheet }}">
</head>
<body>
{{{ header }}}
<div id='container'>
  <div id="background"></div>
  {{#sources?}}
  <div id="jump_to">
    Jump To &hellip;
    <div id="jump_wrapper">
      <div id="jump_page">
        {{#sources}}
          <a class="source" href="{{ url }}">{{ basename }}</a>
        {{/sources}}
      </div>
    </div>
  </div>
  {{/sources?}}
  <div class='section'>
    <div class='docs'><h1>{{ title }}</h1></div>
  </div>
  <div class='clearall'>
  {{#sections}}
  <div class='section' id='section-{{ num }}'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-{{ num }}'>#</a>
      </div>
      {{{ docs_html }}}
    </div>
    <div class='code'>
      {{{ code_html }}}
    </div>
  </div>
  <div class='clearall'></div>
  {{/sections}}
</div>
<script src="{{{ script }}}"></script>
</body>
"""

home_html = """\
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="content-type" content="text/html;charset=utf-8">
  <title>{{{ project_name }}} Documentation</title>
  <link rel="stylesheet" href="{{ stylesheet }}">
</head>
<body>
{{{ header }}}
<div id='container'>
  <div class='section'>
    <div id="home-content" class='docs'>
      {{{ home_page_html }}}
    </div>
  </div>
</div>
<!-- end of container -->
<div class='clearall'></div>
<script src="{{{ script }}}"></script>
</body>
"""
