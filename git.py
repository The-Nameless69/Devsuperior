#-------------------------------------------   Iniciando no Git e GitHub   ---------------------------------------
# O que é o Git?
# O Git é um sistema de versionamentos para controlar versões de algum projeto ou documento, que você estiver produzindo.
# Ele vai te permitir a manter um histórico, voltar a versão anterior e etc.

# O que é GitHub?
# O GitHub é um serviço on-line de hospedagem de projetos gerenciados pelo Git. É como uma rede social de hospedagem de projetos.

#------------------------------------------   Configurando o seu Usuário no Git   -----------------------------------------

# git config --global user.name "Seu nome"
# git config --global user.mail "Seu Email de Cadastro no GitHub"
# git config --list 

#-----------------------------------------   Configurando Chave SSH para o GitHub   ---------------------------------------

# Para gerar uma chave ssh em qualquer sistema operacional, vá a internet e digite (GitHub SSH), depois selecione
# gerar uma nova chave SSH. Para o meu Linux á chave será desta forma abaixo:

# ssh-keygen -t ed25519 -C "seu_email@example.com"
# No seu email, adicione o email que está cadastrado no GitHub.

# Onde ver miha chave SSH?
# A sua chave SSH estará na sub pasta com o nome .ssh, ela estará oculta, assim que localizar estará sua senha privada do ssh
# e sua chave pública, a chave pública terminará com a extensão .pub no final do arquivo abra a sua chave pública em um 
# bloco de notas e copie. No GitHub em configurações na aba SSH and GPG Keys, clique e adicione no link verde a sua chave ssh
# Pública.

#----------------------------------------   Salvar a versão de um projeto no GitHub   -------------------------------------

# git init
# git add .
# git status
# git commit -m "nome do seu projeto"
# git branch -M main
# Crie um repositório no GitHub selecione só se ele irá ser público ou privado, logo após é só criar.
# Logo após criar o seu repositório remoto, lembre-se de selecionar SSH e logo abaixo estará a descrição de como colocar o seu
# repositório remoto no seu Git.Iremos adicionar o que estiver parecido com que está logo abaixo.
# git remote add origin git@github.com:seunomedeusuário/seurepositório.git
# git push -u origin main

#---------------------------------------   Salvando uma nova Versão do Projeto   ------------------------------------------

# git status
# git add .
# git commit -m "Nome do seu projeto novo"
# git push

# O Git push irá enviar para o repositório remoto, que fica no GitHub. Depois disto não tem mais volta.

#--------------------------------------   Verificando Histórico de Versões   ----------------------------------------------

# git log
# git log --oneline

#-------------------------------------   Git Checkout   -------------------------------------------------------------------

# Cada commit possui um código de ratreio que é visto usando o comando git log.
# O último commit modificado é referênciado pela palavara HEAD.
# Usando o comando a seguir, você adiciona este commit para o topo, podendo depois apagar outros commitis a partir dele.

# git checkout Adicione aqui o código do commit que você deseja por no topo

# Os seus arquivos ele volta da versão na qual você escolheu, um exemplo: Se você fez este commit apenas quando a página Html
# estava sem forma, usando este comando acima ele volta de quando era deste jeito.
# Para voltar o branch para o Main novamente, faça o seguinte comando:

# git checkout main

# IMPORTANTE: O Git Checkout é usado para ver a versão anterior do prjeto e você verificar as mudanças que foram feitas
# Não entre no git checkou e mude algo no seu código.
# Se você fez alguma alteração, desfaça as alterações com os seguintes comandos:

# git reset
# git clean -df
# git checkout -- .
# git checkout main


















