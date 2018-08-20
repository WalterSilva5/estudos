
<div class="container">
<!-- Place this tag where you want the Live Helper Chatbox module to render. -->
<div id="lhc_chatbox_embed_container" ></div>

<!-- Place this tag after the Live Helper Chatbox module tag. -->
<script type="text/javascript">
var LHCChatboxOptionsEmbed = {hashchatbox:'empty',identifier:'default'};
(function() {
var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
po.src = '//ntel.000webhostapp.com/chat/index.php/por/chatbox/embed/(chat_height)/220';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
})();
</script>
    <form>
        <div class="col-md-6 form-line">
            <div class="form-group">
                <label for="exampleInputUsername">Seu Nome</label>
                <input type="text" class="float-left form-control" id="" placeholder="Nome">
            </div>
            <div class="form-group">
                <label for="exampleInputEmail">Email</label>
                <input type="email" class="float-left form-control" id="exampleInputEmail" placeholder="Insira Seu Email">
            </div>	
            <div class="form-group">
                <label for="telephone">Celular</label>
                <input type="tel" class="float-left form-control" id="telephone" placeholder="Insira Seu Celular">
            </div>
        </div>
        <div class="col-md-12 float-left">
            <div class="form-group">
                <label for ="description">Mensagem</label>
                <textarea  class="float-left form-control" id="description" placeholder="Insira Sua Mensagem"></textarea>
            </div>
            <div>
                <button type="button" class="btn btn-default submit"><i class="fa fa-paper-plane" aria-hidden="true"></i>Enviar Mensageem</button>
            </div>
        </div>
    </form>
</div>