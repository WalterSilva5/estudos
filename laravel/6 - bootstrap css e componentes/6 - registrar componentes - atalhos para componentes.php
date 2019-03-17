arquivo para registrar atalhos para componentes:
app/providres/appserviceprovidres.php

na parte de usse colocamos:
use Illuminate\support\facades\blade

na função: public function boot()

Blade::componente('components.meuComponente', 'alerta')

e na pagina do template em vez de usarmos @component

usamos @alerta

@alerta é o componente que registrarmos como sendo um componente do arquivo

components.meuComponente

e em vez de usarmos @endcomponent usamos @endalerta