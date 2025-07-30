# Propósito

<div class="wrapper" style="display: flex">
<p>Compilação dos meus códigos do LeetCode e, por ventura, alguma outra plataforma de desafios de programação, como o DataLemur. Apesar do propósito não ser explicar as soluções, tampouco expô-las como uma forma pronta para copiar e colar, para o seu uso, naturalmente pode ser usado para consulta. Podem não ser as formas mais adequadas de se resolver os problemas, mas pode servir como estudo do que você deve ou não fazer.</p>
<p>Os arquivos são tanto exposições das soluções, quanto rascunhos do que eu fiz, por isso parte dos códigos podem estar bagunçados. A minha ideia pe visualizar como que eu evoluo com esses desafios, desenvolvendo programas cada vez mais rápidos e eficientes sozinho. Nenhum dos códigos aqui expostos, a princípio, foram baseados em outras pessoas. A única circunstância em que eu vejo uma outra solução, é se eu mesmo não pude resolver ou, se depois de resolvido, eu quis descobrir uma forma melhor.</p>
</div>

<img src="https://miro.medium.com/v2/resize:fit:1008/1*VOQU8CuPG34Gsd1yJCadOQ.png" style="max-width: 50%" alt="leetcode"></img>

# Explicações Resumidas

## Add Two Numbers

Vamos percorrer as listas ligadas. Enquanto iteramos por elas, construímos uma terceira lista, com cada nó representando a soma dos nós das outras duas, limitada por 10. Aquilo que cair fora do limite, devemos carregar para a próxima a soma, como um residual. Realizamos isso até todas as listas se exaurirem. Para que o programa acesse a nova lista ligada, retornamos o primeiro nó dela.

## Count Hill-Valley

Na minha solução, bem próxima de uma _brute force_, inicializo dois ponteiros ordenados, que vão caminhar a lista. A ideia é que, entre eles, sempre haja ou um vale ou um morro. Portanto, a iteração pela lista ocorre sob a constante verificação de uma subida ou descida. Os ponteiros são deslocados no começo de toda iteração, para nunca testarem regiões planas.

Em uma melhor solução, iteramos linearmente pela lista. A cada ponto de descida ou subida que encontramos, verificamos se é um morro ou vale. Após, esse ponto é fixado por um ponteiro, sendo usado na próxima verificação. Esse processo é repetido até que a lista se esgote. É tremendamente mais fácil, intuitivo e otimizado que a solução anterior (O(n)).

## Smallest Subarray with Maximum Bitwise OR

A minha tentativa de solução se apresentou logicamente correta, mas mal otimizada, o que levou a um Timeout diante de um input muito grande. A solução funcional utiliza alguns malabarismos mentais. Construímos o arranjo dos menores tamanhos necessários para que os subarranjos atinjam o maior bitwise OR, percorrendo apenas uma vez cada número em `nums`. Algumas percepções para que a solução faça sentido:

- O enunciado informa que o tamanho máximo do número é 10^9, o que implica que cada um tem, no máximo, 30 bits.
- A operação OU é capaz apenas de acrescer a string de bits.
- Ao iterar (com _i_) pelos números do último ao primeiro, e pelos bits (com _bit_index_) de cada um desses números, sabemos que o máximo possível do OU para o subarranjo, entre o final de `nums` (n-1, inclusivo) e a posição atual da iteração (_i_), só tende a crescer.
- Encontrar o tamanho do menor subarranjo se trata de encontrar a maior entre as distâncias da posição atual (_i_) e a posição das últimas ocorrências de cada um dos 30 bits, até aquela iteração. Isso acontece por causa da propriedade do OU apenas crescer o máximo. Se queremos o menor tamanho para atingir o máximo, então se trata de encontrar o tamanho do intervalo necessário para que o maior número de bits possíveis sejam 1, porque, para qualquer intervalo maior, mais nenhum bit será adicionado ou removido.
- A observação anterior justifica a iteração do fim para o começo. No final de `nums`, o máximo é menor, porque há menos ocorrências de bits. Na medida com que nos aproximamos do começo, existem mais "ativações" de bits no decorrer do arranjo. Porém, mesmo que o mesmo bit se ative entre diferentes números, como queremos o menor subarranjo, pouco importa o que aconteceu depois da última ocorrência, até o momento _i_.

## Longest Subarray with Maximum Bitwise AND

Tremendamente mais fácil que o anterior. A ideia é retornar o tamanho do maior subarranjo, cuja operação de bit E seja a maior possível. A operação E tem a característica que ela só é capaz de decrescer um número, porque, entre um bit ativo e outro inativo, ela sempre opta pelo inativo. Ou seja, o máximo do arranjo original já se trata do máximo da operação E para algum subarranjo. Sabendo qual é esse máximo, basta contar o maior número de repetições contíguas desse máximo dentro do arranjo. Essa sequência de repetições é o subarranjo que procuramos. Disso, basta verificar qual é a maior das contagens de subarranjos.
