<html>
<head>
    <link href="{{asset('css/app.css')}}" rel="stylesheet">
    <title>Produtos</title>
</head>
<body>
<div class="container bg-info">
    @if($n===1)
        <h1>n = 1</h1>
    @elseif($n[0]===2)
        <h1>n = 2</h1>
    @else
        <h1>n != 1 e n != 2</h1>
    @endif
</div>



<script src="{{asset('js/app.js')}}" rel="text/javascript"></script>
</body>
</html>