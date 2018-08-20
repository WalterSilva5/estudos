    <!-- conteudos do site-->
    <!-- cadastro -->
    <div class="container" style="margin-bottom:30px">
        <div class="page-header">
            <h1>Cadastre-se</h1>
        </div>
        <div class="row">
        <form class = "container recebe-dados"action="http://nteltelecom.com.br/executar.php?acao=assinar" method="post" id="form" onSubmit="return verifica_form(this);">

            <!--div 1 container de organização -->
            <div class="container col-md-12">
            <!-- data de vencimento da mensalidade-->
            <div class="block float-left col-md-6">
            <label for="venc">Dia do vencimento mensal</label>
            <select name="venc" class="form-control h5" id="venc">
                <option value="01"> Todo dia 01 </option>
                <option value="02"> Todo dia 02 </option>
                <option value="03"> Todo dia 03 </option>
                <option value="04"> Todo dia 04 </option>
                <option value="05"> Todo dia 05 </option>
                <option value="06"> Todo dia 06 </option>
                <option value="07"> Todo dia 07 </option>
                <option value="08"> Todo dia 08 </option>
                <option value="09"> Todo dia 09 </option>
                <option value="10"> Todo dia 10 </option>
                <option value="11"> Todo dia 11 </option>
                <option value="12"> Todo dia 12 </option>
                <option value="13"> Todo dia 13 </option>
                <option value="14"> Todo dia 14 </option>
                <option value="15"> Todo dia 15 </option>
                <option value="16"> Todo dia 16 </option>
                <option value="17"> Todo dia 17 </option>
                <option value="18"> Todo dia 18 </option>
                <option value="19"> Todo dia 19 </option>
                <option value="20"> Todo dia 20 </option>
                <option value="21"> Todo dia 21 </option>
                <option value="22"> Todo dia 22 </option>
                <option value="23"> Todo dia 23 </option>
                <option value="24"> Todo dia 24 </option>
                <option value="25"> Todo dia 25 </option>
                <option value="26"> Todo dia 26 </option>
                <option value="27"> Todo dia 27 </option>
                <option value="28"> Todo dia 28 </option>
                <option value="29"> Todo dia 29 </option>
                <option value="30"> Todo dia 30 </option>
                </select>
                </div>
                <!-- fim data de vencimento da mensalidade-->
                
                <!-- Velocidade do Plano -->
                <div class="block float-left col-md-6">
                 <label for="plano">Velocidade do Plano</label>
                <select name="plano" class="form-control h5" id="plano">
                    <!--<option value="1_MEGA"> 1_MEGA</option>
                    <option value="2_MEGAS"> 2_MEGAS</option>-->
                    <option value="3_MEGAS"> 3 MEGAS R$: 40,00</option>
                    <option value="4_MEGAS"> 4 MEGAS R$: 50,00</option>
                    <option value="5_MEGAS"> 5 MEGAS R$: 60,00</option>
                    <option value="6_MEGAS"> 6 MEGAS R$: 70,00</option>
                    <option value="10_MEGAS"> 10 MEGAS R$: 120,00</option>
                </select>
                </div>
                <!-- fim Velocidade do Plano -->
                 </div>
                 <!-- fim da div 1 container de organização -->
                 
                 <!-- div 2 container de organização -->
                <div class="container">
                <!-- login de usuario -->
                <div class="container float-left col-md-6">
                <label for="q">Login</label>
                <input name="q" id="q" value="" class="form-control h5" onKeyUp="buscalogin(this.value)" maxlength="100" df_verificar="sim">
                <!-- fim login de usuario -->
                
                <!-- mensagem caso de erro no login-->
                <div id="msglogin" class="h4 text-danger"></div>
                </div>
                <!-- fim mensagem caso de erro no login -->
                <!-- senha -->
                <div class="container float-left col-md-6">
                <label for="senha">Senha</label>
                <input name="senha" id="senha" class="form-control" value="" maxlength="32" type="password" df_verificar="sim">
                </div>
                <!-- fim senha-->
                </div>
                 <!-- fim div 2 container de organização -->

                 <!-- div 3 container de organização -->
                <div class="container float-left">
                <!-- nome completo-->
                <div class="container">
                <label for="nome">Nome Completo</label>
                <input name="nome" id="nome" class="form-control" value="" maxlength="100" type="text" df_verificar="sim">
                </div>
                <!-- fim nome completo-->

                <!-- e mail -->
                <div class="container">
                <label for="email">E-Mail</label>
                <input name="email" id="email" value="" class="form-control" maxlength="100" type="email" df_verificar="sim" df_validar="email">
                 </div>
                <!-- fim email   -->

                <!-- cnpj cpf -->
                <div class="container">
                <label for="cpf_cnpj">CPF/CNPJ</label>
                <input name="cpf_cnpj" id="cpf_cnpj" class="form-control" value="" maxlength="100" type="text" df_verificar="sim" df_validar="cpf_cnpj" onKeyUp='this.value=this.value.replace(/[^\d]*/gi,"");'>
                </div>
                <!-- fim cnpj cpf -->
                </div>
                <!-- fim div 3 container de organização -->
                
                <!-- div 4 container de organização -->
                <div class="container">
                <!-- rg -->
                <div class="container float-left col-md-4">
                <label for="rg">RG</label>
                <input name="rg" id="rg" class="form-control" maxlength="100" value="" type="number" df_verificar="sim" onKeyUp='this.value=this.value.replace(/[^\d]*/gi,"");'>
                </div>               
                <!-- fim rg -->
                <!-- data de nascimento-->
                <div class="container float-left col-md-4">
                <label for="nascimento">Data de Nascimento</label>
                <input name="nascimento" id="cli_data_nasc" value="" class="form-control" type="date" df_verificar="sim" onKeyPress="return MaskData(this, event)">
                </div>
                <!-- fim data de nascimento-->
                <!--cep-->
                <div class="container float-left col-md-4">
                <label for="cep">CEP</label>
                <input name="cep" type="text" class="form-control" value="" id="cep" onKeyUp="buscacep(this.value)" maxlength="9" onKeyPress="return MaskCEP(this, event)" />
                </div>
                <!--fim cep-->

                <!-- div 4 container organização -->
                <div class="container">
                <!--endereço-->
                <div class="container float-left col-md-10">
                <label for="endereco">Endereço</label>
                <input name="endereco" id="endereco" value="" class="form-control"  type="text" df_verificar="sim">
                </div>
                <!--fim endereço-->
                <!--numero-->
                <div class="container float-left col-md-2">
                <label for="numero">Numero</label>
                <input name="numero" class="form-control" type="text" value="" id="numero" maxlength="10" df_verificar="sim">
                </div>
                <!--fim numero-->
                </div>
                <!-- fim div 4 container organização -->

                <!-- div 5 container organização -->
                <div class="container">
                <!-- complemento -->
                <div class="container float-left col-md-6">
                <label for="complemento">Complemento(Ex.: Andar,  Bloco, etc...)</label>
                <input name="complemento" id="complemento" value="" class="form-control" type="text">
                </div>
                <!-- fim complemento -->
                <!-- bairro -->
                <div class="container float-left col-md-6">
                <label for="bairro">Bairro</label>
                <input name="bairro" id="bairro" class="form-control" value="" maxlength="100" type="text" df_verificar="sim">
                </div>
                <!-- fim bairro -->

                <!-- Cidade -->
                <div class="container float-left col-md-6">
                <label for="cidade">Cidade</label>
                <input name="cidade" id="cidade" class="form-control" value=""  type="text" df_verificar="sim">
                </div>
                <!-- fim cidade -->

                <!-- estado -->
                <div class="container float-left col-md-6">
                <label for="Estado">Estado</label>
                <select name="estado" class="form-control" id="estado">
                    <option value="AC">Acre</option>
                    <option value="AL">Alagoas</option>
                    <option value="AP">Amap&aacute;</option>
                    <option value="AM">Amazonas</option>
                    <option value="BA">Bahia</option>
                    <option value="CE">Cear&aacute;</option>
                    <option value="DF">Distrito Federal</option>
                    <option value="ES">Esp&iacute;rito Santo</option>
                    <option value="GO">Goias</option>
                    <option value="MA">Maranh&atilde;o</option>
                    <option value="MT">Mato Grosso</option>
                    <option value="MS">Mato Grosso do Sul</option>
                    <option value="MG">Minas Gerais</option>
                    <option value="PA">Par&aacute;</option>
                    <option value="PB">Para&iacute;ba</option>
                    <option value="PR">Paran&aacute;</option>
                    <option value="PE" selected=selected>Pernambuco</option>
                    <option value="PI">Piau&iacute;</option>
                    <option value="RJ">Rio de Janeiro</option>
                    <option value="RN">Rio Grande do Norte</option>
                    <option value="RS">Rio Grande do Sul</option>
                    <option value="RO">Rond&ocirc;nia</option>
                    <option value="RR">Roraima</option>
                    <option value="SC">Santa Catarina</option>
                    <option value="SP">S&atilde;o Paulo</option>
                    <option value="SE">Sergipe</option>
                    <option value="TO">Tocantins</option>
                </select>
                </div>
                <!-- fim estado -->

                <!-- Telefone -->
                <div class="container float-left col-md-6">
                <label for="Telefone">Telefone</label>
                <input name="telefone" id="telefone" class="form-control" value="" type="text" onKeyPress="return MaskTelefone(this, event)">
                </div>
                <!-- fim Telefone -->

                <!-- celular -->
                <div class="container float-left col-md-6">
                <label for="celular">Celular</label>
                <input name="celular" id="celular" class="form-control" value="" maxlength="20" type="text" onKeyUp="enviacodigo(this.value)" onKeyPress="return MaskCelular(this, event)" df_verificar="sim">
                </div>
                <!-- fim celular -->

                <!-- inputs q n sei pra q serve -->
                <input name="codigo" type="hidden" id="codigo" value="41EFE412">
                <input name="token" type="hidden" id="token" value="d39445d40355b625646444e4">
                <input name="captchax" type="hidden" id="captchax" value="E2J5VA">
                <input type="hidden" name="token_hotsite" value="26a677e23b95714a953bb5ad17f56a69">
                <!-- fim inputs q n sei pra q serve -->

                <!-- codigo promocional -->
                <div class="container float-left col-md-6">
                <label for="promocod">Codigo Promicional (caso tenha)</label>
                <input name="promocod" id="promocod" class="form-control" value="" type="text">
                </div>
                <!-- fim codigo promocional -->
                </div>
                <!-- fim div 5 container organização -->

                <!-- aceita cadastrar-->
                <div class="container text-center float-left h5">
                <input type="checkbox" name="aceitou" id="aceitou" value="sim">
                Declaro que li e aceito o <strong><a href="contrato.html" target="_blank" onClick="window.open(this.href, this.target, 'width=740,height=420,scrollbars=yes'); return false;">contrato</a></strong> do provedor.
                </div>
                <!-- fim aceita cadastrar-->

                <!-- cadastrar ou limpar-->
                <div class="container float-left text-center">
                <input name="enviar" class="botao btn btn-warning" id="enviar" value="Cadastrar" alt="Enviar" type="submit">
                <input name="limpar" class="botao btn btn-warning" alt="Limpar" id="limpar" value="Limpar" type="reset">
                </div>
                <!-- fim cadastrar ou limpar-->
                </div>
            </form>
        </div>
    </div>

    <!-- fim cadastro -->
    <!-- fim conteudos do site-->