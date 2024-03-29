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
      <li><a href="{{html_file_name}}">{{pretty_name}}</a></li>
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
  <style type="text/css">
    /*--------------------- Layout and Typography ----------------------------*/
    body {
      font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, FreeSerif, serif;
      font-size: 15px;
      line-height: 24px;
      color: #252519;
      margin: 0; padding: 0;
    }
    a {
      color: #261a3b;
    }
      a:visited {
        color: #261a3b;
      }
    p {
      margin: 0 0 15px 0;
    }
    h1, h2, h3, h4, h5, h6 {
      margin: 40px 0 15px 0;
    }
    h2, h3, h4, h5, h6 {
        margin-top: 0;
      }
    #container, div.section {
      position: relative;
    }
    #background {
      position: fixed;
      top: 0; left: 525px; right: 0; bottom: 0;
      background: #f5f5ff;
      border-left: 1px solid #e5e5ee;
      z-index: -1;
    }
    #flybar {
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
    #jump_to, #jump_page {
      background: white;
      -webkit-box-shadow: 0 0 25px #777; -moz-box-shadow: 0 0 25px #777;
      -webkit-border-bottom-left-radius: 5px; -moz-border-radius-bottomleft: 5px;
      font: 10px Arial;
      text-transform: uppercase;
      cursor: pointer;
      text-align: right;
    }
    #jump_to, #jump_wrapper {
      position: fixed;
      right: 0; top: 0;
      padding: 5px 10px;
    }
      #jump_wrapper {
        padding: 0;
        display: none;
      }
        #jump_to:hover #jump_wrapper {
          display: block;
        }
        #jump_page {
          padding: 5px 0 3px;
          margin: 0 0 25px 25px;
        }
          #jump_page .source {
            display: block;
            padding: 5px 10px;
            text-decoration: none;
            border-top: 1px solid #eee;
          }
            #jump_page .source:hover {
              background: #f5f5ff;
            }
            #jump_page .source:first-child {
            }
    div.docs {
      float: left;
      overflow: hidden;
      max-width: 450px;
      min-width: 450px;
      min-height: 5px;
      padding: 10px 25px 1px 50px;
      vertical-align: top;
      text-align: left;
    }
    
    #home-content {
      max-width: 600px;
      min-width: 500px;
    }
    
      .docs pre {
        margin: 15px 0 15px;
        padding-left: 15px;
      }
      .docs p tt, .docs p code {
        background: #f8f8ff;
        border: 1px solid #dedede;
        padding: 0 0.2em;
      }
      .octowrap {
        position: relative;
      }
        .octothorpe {
          font: 12px Arial;
          text-decoration: none;
          color: #454545;
          position: absolute;
          top: 3px; left: -20px;
          padding: 1px 2px;
          opacity: 0;
          -webkit-transition: opacity 0.2s linear;
        }
          div.docs:hover .octothorpe {
            opacity: 1;
          }
    div.code {
      margin-left: 500px;
      padding: 14px 0px 16px 50px;
      vertical-align: top;
      word-wrap:break-word;
    }
      .code pre, .docs p code {
        font-size: 12px;
      }
        pre, tt, code {
          font-size: 12px;
          line-height: 18px;
          font-family: Menlo, Monaco, Consolas, "Lucida Console", monospace;
          margin: 0; padding: 0;
        }
    div.clearall {
        clear: both;
    }
    
    
    /*---------------------- Syntax Highlighting -----------------------------*/
    td.linenos { background-color: #f0f0f0; padding-right: 10px; }
    span.lineno { background-color: #f0f0f0; padding: 0 5px 0 5px; }
    body .hll { background-color: #ffffcc }
    body .c { color: #408080; font-style: italic }  /* Comment */
    body .err { border: 1px solid #FF0000 }         /* Error */
    body .k { color: #954121 }                      /* Keyword */
    body .o { color: #666666 }                      /* Operator */
    body .cm { color: #408080; font-style: italic } /* Comment.Multiline */
    body .cp { color: #BC7A00 }                     /* Comment.Preproc */
    body .c1 { color: #408080; font-style: italic } /* Comment.Single */
    body .cs { color: #408080; font-style: italic } /* Comment.Special */
    body .gd { color: #A00000 }                     /* Generic.Deleted */
    body .ge { font-style: italic }                 /* Generic.Emph */
    body .gr { color: #FF0000 }                     /* Generic.Error */
    body .gh { color: #000080; font-weight: bold }  /* Generic.Heading */
    body .gi { color: #00A000 }                     /* Generic.Inserted */
    body .go { color: #808080 }                     /* Generic.Output */
    body .gp { color: #000080; font-weight: bold }  /* Generic.Prompt */
    body .gs { font-weight: bold }                  /* Generic.Strong */
    body .gu { color: #800080; font-weight: bold }  /* Generic.Subheading */
    body .gt { color: #0040D0 }                     /* Generic.Traceback */
    body .kc { color: #954121 }                     /* Keyword.Constant */
    body .kd { color: #954121; font-weight: bold }  /* Keyword.Declaration */
    body .kn { color: #954121; font-weight: bold }  /* Keyword.Namespace */
    body .kp { color: #954121 }                     /* Keyword.Pseudo */
    body .kr { color: #954121; font-weight: bold }  /* Keyword.Reserved */
    body .kt { color: #B00040 }                     /* Keyword.Type */
    body .m { color: #666666 }                      /* Literal.Number */
    body .s { color: #219161 }                      /* Literal.String */
    body .na { color: #7D9029 }                     /* Name.Attribute */
    body .nb { color: #954121 }                     /* Name.Builtin */
    body .nc { color: #0000FF; font-weight: bold }  /* Name.Class */
    body .no { color: #880000 }                     /* Name.Constant */
    body .nd { color: #AA22FF }                     /* Name.Decorator */
    body .ni { color: #999999; font-weight: bold }  /* Name.Entity */
    body .ne { color: #D2413A; font-weight: bold }  /* Name.Exception */
    body .nf { color: #0000FF }                     /* Name.Function */
    body .nl { color: #A0A000 }                     /* Name.Label */
    body .nn { color: #0000FF; font-weight: bold }  /* Name.Namespace */
    body .nt { color: #954121; font-weight: bold }  /* Name.Tag */
    body .nv { color: #19469D }                     /* Name.Variable */
    body .ow { color: #AA22FF; font-weight: bold }  /* Operator.Word */
    body .w { color: #bbbbbb }                      /* Text.Whitespace */
    body .mf { color: #666666 }                     /* Literal.Number.Float */
    body .mh { color: #666666 }                     /* Literal.Number.Hex */
    body .mi { color: #666666 }                     /* Literal.Number.Integer */
    body .mo { color: #666666 }                     /* Literal.Number.Oct */
    body .sb { color: #219161 }                     /* Literal.String.Backtick */
    body .sc { color: #219161 }                     /* Literal.String.Char */
    body .sd { color: #219161; font-style: italic } /* Literal.String.Doc */
    body .s2 { color: #219161 }                     /* Literal.String.Double */
    body .se { color: #BB6622; font-weight: bold }  /* Literal.String.Escape */
    body .sh { color: #219161 }                     /* Literal.String.Heredoc */
    body .si { color: #BB6688; font-weight: bold }  /* Literal.String.Interpol */
    body .sx { color: #954121 }                     /* Literal.String.Other */
    body .sr { color: #BB6688 }                     /* Literal.String.Regex */
    body .s1 { color: #219161 }                     /* Literal.String.Single */
    body .ss { color: #19469D }                     /* Literal.String.Symbol */
    body .bp { color: #954121 }                     /* Name.Builtin.Pseudo */
    body .vc { color: #19469D }                     /* Name.Variable.Class */
    body .vg { color: #19469D }                     /* Name.Variable.Global */
    body .vi { color: #19469D }                     /* Name.Variable.Instance */
    body .il { color: #666666 }                     /* Literal.Number.Integer.Long */
    
    /* Body */
    #container {
      margin: 20px 0px 0px 0px;
    }
    
    #home-content {
      margin: 40px 0px 0px 0px;
    }
    
    .hide {
      display: none !important;
    }
    
    /* STICKY HEADER */
    
    #flybar {
      position: fixed;
      z-index: 100;
      height: 40px;
      min-width: 745px;
      left: 0;
      right: 0;
      top: 0;
      padding-left: 360px;
      background: #EEE;
      background: -webkit-gradient(linear, left top, left bottom, from(#F8F8F8), to(#DADADA));
      background: -moz-linear-gradient(top, #F8F8F8, #DADADA);
      border-top: 15px solid black;
      border-bottom: 1px solid #888;
      -webkit-box-shadow: 0 3px 5px rgba(0,0,0,0.1);
      -moz-box-shadow: 0 3px 5px rgba(0,0,0,0.1);
      box-shadow: 0 3px 5px rgba(0,0,0,0.1);
    }
    
    #flybar a {
      text-decoration: none;
    }
    
    #nav-logo {
      display: block;
      height: 30px;
      position: absolute;
      top: 7px;
      left: 10px;
      font-weight: bold;
    }
    
    .flybar-language {
      display: block;
      float: left;
      position: relative;
    }
    
    .flybar-button:hover, .flybar-button.active, .flybar-nav:hover .flybar-button, .flybar-nav.active .flybar-button {
      background-color: #ffffff;
      border-left: 1px solid #BBB;
      border-right: 1px solid #BBB;
    }
    
    .flybar-button {
      text-align: center;
      text-transform: uppercase;
      font-size: 12px;
      padding: 0 1em;
      line-height: 40px;
      border-right: 1px solid transparent;
      border-left: 1px solid transparent;
      text-decoration: none;
      font-weight: bold;
      color: black;
      cursor: pointer;
    }
    
    .flybar-language .flybar-button {
      float: left;
      clear: none;
      border-right: 1px solid transparent;
      border-left: 1px solid transparent;
      min-width: 80px;
      margin-left: -1px;
    }
    
    .open .flybar-button {
    
    
      color: white;
      background-color: #999;
      border-color: #999;
      border-bottom: 0px;
    }
    
    /* DROP DOWN MENU */
    
    .open .dropdown-menu {
      display: block;
    }
    
    .dropdown-menu {
      position: fixed;
      top: 55px;
      overflow-y: auto;
      height: 80%;
      z-index: 1000;
      display: none;
      float: left;
      min-width: 220px;
      padding: 4px 0;
      margin: 1px 0 0 -1px;
      list-style: none;
      background-color: #ffffff;
      border: 1px solid #ccc;
      border: 1px solid rgba(0, 0, 0, 0.2);
      border-top-style: none;
    
      *border-right-width: 2px;
      *border-bottom-width: 2px;
    
      -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
      -moz-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
      box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
      -webkit-background-clip: padding-box;
      -moz-background-clip: padding;
      background-clip: padding-box;
    }
    
    .dropdown-menu a {
      display: block;
      padding: 3px 15px;
      clear: both;
      font-weight: normal;
      line-height: 18px;
      color: #333;
      white-space: nowrap;
    }
    
    .dropdown-menu li > a:hover, .dropdown-menu .active > a, .dropdown-menu .active > a:hover {
      color: white;
      text-decoration: none;
      background-color: #08C;
    }
    
    li {
      line-height: 18px;
      display: list-item;
    }
    
    .caret {
      margin: 18px 2px;
      font-weight: bold;
      display: inline-block;
      width: 0;
      height: 0;
      vertical-align: top;
      border-top: 4px solid black;
      border-right: 4px solid transparent;
      border-left: 4px solid transparent;
      content: "";
      opacity: 0.3;
      filter: alpha(opacity=30);
    }
    
    .open .caret {
      border-top-color: white;
      border-bottom-color: white;
      opacity: 1;
      filter: alpha(opacity=100);
    }
    
    .nav-tabs .open .dropdown-toggle {
      color: white;
      background-color: #999;
      border-color: #999;
    }
  </style>
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
<script>
// Provides basic UI utilities
var UIUtil = {

    // After opening an element, we hide it if the user another part of the app
    hideWhenUserClicksAway: function(selector, onClickAway) {
        $('body').bind('click', function(e) {
            // If the user clicks outside of the form, hide it.
            closestElements = $(e.target).closest(selector);
            elementsOfInterest = $(selector);

            // If the element clicked isn't part of what was clicked, hide the element
            if(closestElements.length == 0) {
                if(elementsOfInterest.is(':visible')) {
                    if(typeof(onClickAway) == 'function') onClickAway(selector, e);
                    else elementsOfInterest.hide();
                }
            }
        });
    }
}

var Docs = {
    init: function() {
        this.bindToUIActions();
    },

    bindToUIActions: function() {
        $('#pages-dropdown,#functions-dropdown').on('click', this.showDropdownMenu);

        UIUtil.hideWhenUserClicksAway('#pages-dropdown,#functions-dropdown', this.hideDropdownMenu);
    },

    showDropdownMenu: function() {
        Docs.hideDropdownMenu();
        $(this).closest('.dropdown').addClass('open');
    },

    hideDropdownMenu: function() {
        $('div.dropdown').removeClass("open");
    }

}

$(document).ready(function() {
    Docs.init();
});

</script>

</body>
"""

home_html = """\
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="content-type" content="text/html;charset=utf-8">
  <title>{{{ project_name }}} Documentation</title>
  <link rel="stylesheet" href="{{ stylesheet }}">
  <style type="text/css">
    /*--------------------- Layout and Typography ----------------------------*/
    body {
      font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, FreeSerif, serif;
      font-size: 15px;
      line-height: 24px;
      color: #252519;
      margin: 0; padding: 0;
    }
    a {
      color: #261a3b;
    }
      a:visited {
        color: #261a3b;
      }
    p {
      margin: 0 0 15px 0;
    }
    h1, h2, h3, h4, h5, h6 {
      margin: 40px 0 15px 0;
    }
    h2, h3, h4, h5, h6 {
        margin-top: 0;
      }
    #container, div.section {
      position: relative;
    }
    #background {
      position: fixed;
      top: 0; left: 525px; right: 0; bottom: 0;
      background: #f5f5ff;
      border-left: 1px solid #e5e5ee;
      z-index: -1;
    }
    #flybar {
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
    #jump_to, #jump_page {
      background: white;
      -webkit-box-shadow: 0 0 25px #777; -moz-box-shadow: 0 0 25px #777;
      -webkit-border-bottom-left-radius: 5px; -moz-border-radius-bottomleft: 5px;
      font: 10px Arial;
      text-transform: uppercase;
      cursor: pointer;
      text-align: right;
    }
    #jump_to, #jump_wrapper {
      position: fixed;
      right: 0; top: 0;
      padding: 5px 10px;
    }
      #jump_wrapper {
        padding: 0;
        display: none;
      }
        #jump_to:hover #jump_wrapper {
          display: block;
        }
        #jump_page {
          padding: 5px 0 3px;
          margin: 0 0 25px 25px;
        }
          #jump_page .source {
            display: block;
            padding: 5px 10px;
            text-decoration: none;
            border-top: 1px solid #eee;
          }
            #jump_page .source:hover {
              background: #f5f5ff;
            }
            #jump_page .source:first-child {
            }
    div.docs {
      float: left;
      overflow: hidden;
      max-width: 450px;
      min-width: 450px;
      min-height: 5px;
      padding: 10px 25px 1px 50px;
      vertical-align: top;
      text-align: left;
    }
    
    #home-content {
      max-width: 600px;
      min-width: 500px;
    }
    
      .docs pre {
        margin: 15px 0 15px;
        padding-left: 15px;
      }
      .docs p tt, .docs p code {
        background: #f8f8ff;
        border: 1px solid #dedede;
        padding: 0 0.2em;
      }
      .octowrap {
        position: relative;
      }
        .octothorpe {
          font: 12px Arial;
          text-decoration: none;
          color: #454545;
          position: absolute;
          top: 3px; left: -20px;
          padding: 1px 2px;
          opacity: 0;
          -webkit-transition: opacity 0.2s linear;
        }
          div.docs:hover .octothorpe {
            opacity: 1;
          }
    div.code {
      margin-left: 500px;
      padding: 14px 0px 16px 50px;
      vertical-align: top;
      word-wrap:break-word;
    }
      .code pre, .docs p code {
        font-size: 12px;
      }
        pre, tt, code {
          font-size: 12px;
          line-height: 18px;
          font-family: Menlo, Monaco, Consolas, "Lucida Console", monospace;
          margin: 0; padding: 0;
        }
    div.clearall {
        clear: both;
    }
    
    
    /*---------------------- Syntax Highlighting -----------------------------*/
    td.linenos { background-color: #f0f0f0; padding-right: 10px; }
    span.lineno { background-color: #f0f0f0; padding: 0 5px 0 5px; }
    body .hll { background-color: #ffffcc }
    body .c { color: #408080; font-style: italic }  /* Comment */
    body .err { border: 1px solid #FF0000 }         /* Error */
    body .k { color: #954121 }                      /* Keyword */
    body .o { color: #666666 }                      /* Operator */
    body .cm { color: #408080; font-style: italic } /* Comment.Multiline */
    body .cp { color: #BC7A00 }                     /* Comment.Preproc */
    body .c1 { color: #408080; font-style: italic } /* Comment.Single */
    body .cs { color: #408080; font-style: italic } /* Comment.Special */
    body .gd { color: #A00000 }                     /* Generic.Deleted */
    body .ge { font-style: italic }                 /* Generic.Emph */
    body .gr { color: #FF0000 }                     /* Generic.Error */
    body .gh { color: #000080; font-weight: bold }  /* Generic.Heading */
    body .gi { color: #00A000 }                     /* Generic.Inserted */
    body .go { color: #808080 }                     /* Generic.Output */
    body .gp { color: #000080; font-weight: bold }  /* Generic.Prompt */
    body .gs { font-weight: bold }                  /* Generic.Strong */
    body .gu { color: #800080; font-weight: bold }  /* Generic.Subheading */
    body .gt { color: #0040D0 }                     /* Generic.Traceback */
    body .kc { color: #954121 }                     /* Keyword.Constant */
    body .kd { color: #954121; font-weight: bold }  /* Keyword.Declaration */
    body .kn { color: #954121; font-weight: bold }  /* Keyword.Namespace */
    body .kp { color: #954121 }                     /* Keyword.Pseudo */
    body .kr { color: #954121; font-weight: bold }  /* Keyword.Reserved */
    body .kt { color: #B00040 }                     /* Keyword.Type */
    body .m { color: #666666 }                      /* Literal.Number */
    body .s { color: #219161 }                      /* Literal.String */
    body .na { color: #7D9029 }                     /* Name.Attribute */
    body .nb { color: #954121 }                     /* Name.Builtin */
    body .nc { color: #0000FF; font-weight: bold }  /* Name.Class */
    body .no { color: #880000 }                     /* Name.Constant */
    body .nd { color: #AA22FF }                     /* Name.Decorator */
    body .ni { color: #999999; font-weight: bold }  /* Name.Entity */
    body .ne { color: #D2413A; font-weight: bold }  /* Name.Exception */
    body .nf { color: #0000FF }                     /* Name.Function */
    body .nl { color: #A0A000 }                     /* Name.Label */
    body .nn { color: #0000FF; font-weight: bold }  /* Name.Namespace */
    body .nt { color: #954121; font-weight: bold }  /* Name.Tag */
    body .nv { color: #19469D }                     /* Name.Variable */
    body .ow { color: #AA22FF; font-weight: bold }  /* Operator.Word */
    body .w { color: #bbbbbb }                      /* Text.Whitespace */
    body .mf { color: #666666 }                     /* Literal.Number.Float */
    body .mh { color: #666666 }                     /* Literal.Number.Hex */
    body .mi { color: #666666 }                     /* Literal.Number.Integer */
    body .mo { color: #666666 }                     /* Literal.Number.Oct */
    body .sb { color: #219161 }                     /* Literal.String.Backtick */
    body .sc { color: #219161 }                     /* Literal.String.Char */
    body .sd { color: #219161; font-style: italic } /* Literal.String.Doc */
    body .s2 { color: #219161 }                     /* Literal.String.Double */
    body .se { color: #BB6622; font-weight: bold }  /* Literal.String.Escape */
    body .sh { color: #219161 }                     /* Literal.String.Heredoc */
    body .si { color: #BB6688; font-weight: bold }  /* Literal.String.Interpol */
    body .sx { color: #954121 }                     /* Literal.String.Other */
    body .sr { color: #BB6688 }                     /* Literal.String.Regex */
    body .s1 { color: #219161 }                     /* Literal.String.Single */
    body .ss { color: #19469D }                     /* Literal.String.Symbol */
    body .bp { color: #954121 }                     /* Name.Builtin.Pseudo */
    body .vc { color: #19469D }                     /* Name.Variable.Class */
    body .vg { color: #19469D }                     /* Name.Variable.Global */
    body .vi { color: #19469D }                     /* Name.Variable.Instance */
    body .il { color: #666666 }                     /* Literal.Number.Integer.Long */
    
    /* Body */
    #container {
      margin: 20px 0px 0px 0px;
    }
    
    #home-content {
      margin: 40px 0px 0px 0px;
    }
    
    .hide {
      display: none !important;
    }
    
    /* STICKY HEADER */
    
    #flybar {
      position: fixed;
      z-index: 100;
      height: 40px;
      min-width: 745px;
      left: 0;
      right: 0;
      top: 0;
      padding-left: 360px;
      background: #EEE;
      background: -webkit-gradient(linear, left top, left bottom, from(#F8F8F8), to(#DADADA));
      background: -moz-linear-gradient(top, #F8F8F8, #DADADA);
      border-top: 15px solid black;
      border-bottom: 1px solid #888;
      -webkit-box-shadow: 0 3px 5px rgba(0,0,0,0.1);
      -moz-box-shadow: 0 3px 5px rgba(0,0,0,0.1);
      box-shadow: 0 3px 5px rgba(0,0,0,0.1);
    }
    
    #flybar a {
      text-decoration: none;
    }
    
    #nav-logo {
      display: block;
      height: 30px;
      position: absolute;
      top: 7px;
      left: 10px;
      font-weight: bold;
    }
    
    .flybar-language {
      display: block;
      float: left;
      position: relative;
    }
    
    .flybar-button:hover, .flybar-button.active, .flybar-nav:hover .flybar-button, .flybar-nav.active .flybar-button {
      background-color: #ffffff;
      border-left: 1px solid #BBB;
      border-right: 1px solid #BBB;
    }
    
    .flybar-button {
      text-align: center;
      text-transform: uppercase;
      font-size: 12px;
      padding: 0 1em;
      line-height: 40px;
      border-right: 1px solid transparent;
      border-left: 1px solid transparent;
      text-decoration: none;
      font-weight: bold;
      color: black;
      cursor: pointer;
    }
    
    .flybar-language .flybar-button {
      float: left;
      clear: none;
      border-right: 1px solid transparent;
      border-left: 1px solid transparent;
      min-width: 80px;
      margin-left: -1px;
    }
    
    .open .flybar-button {
    
    
      color: white;
      background-color: #999;
      border-color: #999;
      border-bottom: 0px;
    }
    
    /* DROP DOWN MENU */
    
    .open .dropdown-menu {
      display: block;
    }
    
    .dropdown-menu {
      position: fixed;
      top: 55px;
      overflow-y: auto;
      height: 80%;
      z-index: 1000;
      display: none;
      float: left;
      min-width: 220px;
      padding: 4px 0;
      margin: 1px 0 0 -1px;
      list-style: none;
      background-color: #ffffff;
      border: 1px solid #ccc;
      border: 1px solid rgba(0, 0, 0, 0.2);
      border-top-style: none;
    
      *border-right-width: 2px;
      *border-bottom-width: 2px;
    
      -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
      -moz-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
      box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
      -webkit-background-clip: padding-box;
      -moz-background-clip: padding;
      background-clip: padding-box;
    }
    
    .dropdown-menu a {
      display: block;
      padding: 3px 15px;
      clear: both;
      font-weight: normal;
      line-height: 18px;
      color: #333;
      white-space: nowrap;
    }
    
    .dropdown-menu li > a:hover, .dropdown-menu .active > a, .dropdown-menu .active > a:hover {
      color: white;
      text-decoration: none;
      background-color: #08C;
    }
    
    li {
      line-height: 18px;
      display: list-item;
    }
    
    .caret {
      margin: 18px 2px;
      font-weight: bold;
      display: inline-block;
      width: 0;
      height: 0;
      vertical-align: top;
      border-top: 4px solid black;
      border-right: 4px solid transparent;
      border-left: 4px solid transparent;
      content: "";
      opacity: 0.3;
      filter: alpha(opacity=30);
    }
    
    .open .caret {
      border-top-color: white;
      border-bottom-color: white;
      opacity: 1;
      filter: alpha(opacity=100);
    }
    
    .nav-tabs .open .dropdown-toggle {
      color: white;
      background-color: #999;
      border-color: #999;
    }
  </style>

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
<script>
// Provides basic UI utilities
var UIUtil = {

    // After opening an element, we hide it if the user another part of the app
    hideWhenUserClicksAway: function(selector, onClickAway) {
        $('body').bind('click', function(e) {
            // If the user clicks outside of the form, hide it.
            closestElements = $(e.target).closest(selector);
            elementsOfInterest = $(selector);

            // If the element clicked isn't part of what was clicked, hide the element
            if(closestElements.length == 0) {
                if(elementsOfInterest.is(':visible')) {
                    if(typeof(onClickAway) == 'function') onClickAway(selector, e);
                    else elementsOfInterest.hide();
                }
            }
        });
    }
}

var Docs = {
    init: function() {
        this.bindToUIActions();
    },

    bindToUIActions: function() {
        $('#pages-dropdown,#functions-dropdown').on('click', this.showDropdownMenu);

        UIUtil.hideWhenUserClicksAway('#pages-dropdown,#functions-dropdown', this.hideDropdownMenu);
    },

    showDropdownMenu: function() {
        Docs.hideDropdownMenu();
        $(this).closest('.dropdown').addClass('open');
    },

    hideDropdownMenu: function() {
        $('div.dropdown').removeClass("open");
    }

}

$(document).ready(function() {
    Docs.init();
});

</script>
</body>
"""
