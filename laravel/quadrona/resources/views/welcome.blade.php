<!DOCTYPE html>
<html>
    <meta charset="UTF-8">
    <header><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <!-- Adicionando Javascript -->
    <script>
    
        function limpa_formulário_cep() {
                //Limpa valores do formulário de cep.
                document.getElementById('rua').value=("");
                document.getElementById('bairro').value=("");
                document.getElementById('cidade').value=("");
                document.getElementById('uf').value=("");
                document.getElementById('ibge').value=("");
        }
    
        function meu_callback(conteudo) {
            if (!("erro" in conteudo)) {
                //Atualiza os campos com os valores.
                document.getElementById('rua').value=(conteudo.logradouro);
                document.getElementById('bairro').value=(conteudo.bairro);
                document.getElementById('cidade').value=(conteudo.localidade);
                document.getElementById('uf').value=(conteudo.uf);
                document.getElementById('ibge').value=(conteudo.ibge);
            } //end if.
            else {
                //CEP não Encontrado.
                limpa_formulário_cep();
                alert("CEP não encontrado.");
            }
        }
            
        function pesquisacep(valor) {
    
            //Nova variável "cep" somente com dígitos.
            var cep = valor.replace(/\D/g, '');
    
            //Verifica se campo cep possui valor informado.
            if (cep != "") {
    
                //Expressão regular para validar o CEP.
                var validacep = /^[0-9]{8}$/;
    
                //Valida o formato do CEP.
                if(validacep.test(cep)) {
    
                    //Preenche os campos com "..." enquanto consulta webservice.
                    document.getElementById('rua').value="...";
                    document.getElementById('bairro').value="...";
                    document.getElementById('cidade').value="...";
                    document.getElementById('uf').value="...";
                    document.getElementById('ibge').value="...";
    
                    //Cria um elemento javascript.
                    var script = document.createElement('script');
    
                    //Sincroniza com o callback.
                    script.src = 'https://viacep.com.br/ws/'+ cep + '/json/?callback=meu_callback';
    
                    //Insere script no documento e carrega o conteúdo.
                    document.body.appendChild(script);
    
                } //end if.
                else {
                    //cep é inválido.
                    limpa_formulário_cep();
                    alert("Formato de CEP inválido.");
                }
            } //end if.
            else {
                //cep sem valor, limpa formulário.
                limpa_formulário_cep();
            }
        };
    
        </script>
<style>
    .texto{
        font-size: 90px;
        text-align: center;
        color: orange;
    }
    .centro{
        width: 60%;
        position: relative;
        left: 20%;

        border:solid 2px;
        border-color: black;
        border-radius: 60px;
    }
    .borda{
        width: 50%;
        position: absolute;
        left: 20%;

        
    }
    </style>
    </header>
    <body>
        <form action="{{route('criar')}}" method="post">
            @csrf
        <hr>
        <div class="centro">
        <div class = "borda">
        <h5 class= "texto" style="text-align: center;">QUADRONA</h5>
            <div class="col-md-6">
              <label for="inputEmail4" class="form-label">Email</label  size="100">
              <input class="form-control" name= "email" type="email" id="inputEmail4">
            </div>
            <div class="col-md-6">
              <label for="inputPassword4" class="form-label">senha</label  size="100">
              <input class="form-control" name= "senha" type="password" id="inputPassword4">
            
            </div>
            <div class="col-12">
             
            
          <!-- Inicio do formulario -->
        <label class="form-label"> Nome:
        <input class="form-control" name="nome" type="text" id="nome" size="100" /></label><br />
        <label class="form-label"> Telefone:
        <input class="form-control" name="telefone" type="text" id="telefone" size="100" /></label><br />
        <label class="form-label"> Cep:
        <input class="form-control" name="cep" type="text" id="cep" value="" size="100"
               onblur="pesquisacep(this.value);" /></label><br />
        <label class="form-label"> Rua:
        <input class="form-control" name="rua" type="text" id="rua" size="100" /></label><br />
        <label class="form-label"> Bairro:
        <input class="form-control" name="bairro" type="text" id="bairro" size="100" /></label><br />
        <label class="form-label"> Cidade:
        <input class="form-control" name="cidade" type="text" id="cidade" size="100" /></label><br />
        <label class="form-label"> Estado:
        <input class="form-control" name="uf" type="text" id="uf" size="100" /></label><br />
        <label class="form-label"> Numero:
        <input class="form-control" name="numero" type="text" id="numero" size="100" /></label><br />
        <label class="form-label"> Complemento:
        <input class="form-control" name="complemento" type="text" id="complemento" size="100" /></label><br />

        <input class="form-control" name="ibge" type="HIDDEN" id="ibge" size="100" /></label><br />
      </div>
      <div class="form-check">
        <input class="form-check-input" type="checkbox" id="gridCheck">
        <label class="form-check-label" for="gridCheck">
          salvar
        </label>
      </div>
      <div class="col-12">
        <button type="submit" class="btn btn-primary">Cadastrar</button>
      </div>
      
      </form>
    </div>
    </body>
<html>