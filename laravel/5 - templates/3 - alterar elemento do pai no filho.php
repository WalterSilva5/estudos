colocamos um elemento blade com nome no pai
por exemplo no titulo

<title>@yield('titulo')</title>

e no filho colocamos um elemento que altera esse titulo

por exemplo

@section('titulo', 'este titulo foi alterado')