O que é ABC?
ABC significa:
Abstract Base Class
Ela não é usada diretamente, apenas serve para outras classes herdarem dela.
Exemplo da vida real:
📐 Planta de uma casa
Não é a casa — é o modelo para construir casas.

abstractmethod significa:
um método que é obrigatório implementar depois.
Se eu disser:
Toda a bicicleta tem de ter pedais
Quem construir uma bicicleta tem obrigatoriamente de criar pedais.

from typing import Any, List, Dict, Union, Optional
Aqui estás a importar ferramentas da biblioteca typing.
Esta biblioteca serve para:
explicar que tipo de dados uma função recebe ou devolve.
Isto chama-se type hints.
Eles não mudam o funcionamento, apenas ajudam a entender o código.
any, list, dict, union(um ou outro), optional (algo ou None)

class DataProcessor(ABC)
esta classe é uma Abstract Base Class
Ou seja:
❌ Não deve ser usada diretamente
✅ Serve para outras classes herdarem
DataProcessor
   ↑
CSVProcessor
JSONProcessor
APIProcessor

pass significa:
não faz nada (placeholder)
É usado quando o método ainda não tem implementação.

class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            total = 0
            count = 0
            for item in data:
                total += item
                count += 1
            return count > 0
        except TypeError:
            return False
verifica se os elementos sao iteraveis 
(ou seja somaveis, se for str nao soma com o 0 do total)
o count serve para dizer que ha mais do que 1 elemento,
que o parametro nao esta vazio
typeerror diz logo que ha um problema int ou str

def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: Invalid numeric data"
        try:
            total = 0
            count = 0
            for nbr in data:
                total += nbr
                count += 1
            avg = total / count
            return f"Processed {count} numeric values, sum={total}, avg={avg}"
        except Exception as e:
            return f"Error during processing: {e}"
primeiro fazemos a verificaçao do validate
depois contamos e somamos
o except ja verifica todos os erros, por exemplo dividir por 0
o exception nao esconde o erro porque esta com o {e}, ou seja,
ele depois diz qual foi o erro

class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            return ":" in (data + '')
        except TypeError:
            return False
aqui dizemos que sempre que exista :
(return ":" in (data + ''))
Aqui há duas coisas a acontecer.
Isto tenta concatenar uma string vazia. só funciona se data for texto.
":" in texto
Isto verifica se existe : dentro do texto.

def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: Invalid log format"
        try:
            parts = data.split(":", 1)
            level = parts[0]
            message = parts[1].strip()
            return f"{level}|{message}"
        except Exception as e:
            return f"Error: {e}"
divide-se o que esta antes e depois do :
para a seguir no formato decidirmos o que escrever
O Problema do :: No process(), tu recebes algo como "ERROR: Connection timeout". 
Se o process() retornar a string exatamente assim, quando ela chegar ao 
format_output(), tu terás de procurar o : novamente. O problema é que, se a mensagem 
original for algo como "INFO: Erro no servidor: porta 80", o : aparece duas vezes 
e o teu código pode ficar confuso sobre onde termina o nível e onde começa a mensagem. 😵‍💫

Ao usar o |, cria-se um protocolo interno onde dizemos ao sistema: "Não importa o 
que venha antes, trata isso como a Etiqueta (Level) e o que vem depois como a Mensagem".
Isso permite que o teu LogProcessor seja flexível. Se amanhã o Nexus decidir criar um 
nível chamado CRITICAL ou DEBUG, o teu código não precisa de ser alterado, porque ele 
já sabe separar as duas partes através desse "muro" que construíste. 🧱

def format_output(self, result: str) -> str:
        try:
            parts = result.split("|")
            level = parts[0]
            message = parts[1]
            if level == "ERROR":
                prefix = "[ALERT]"
            else:
                prefix = "[INFO]"
            return f"Output: {prefix} {level} level detected: {message}"
        except Exception as e:
            return f"Error: {e}"
aqui dividimos consoante o que ficou dividido com o |


Quando escrevemos num_proc = NumericProcessor(), os parênteses vazios significam que estamos 
a chamar o construtor da classe (o método __init__) sem passar nenhum argumento inicial.

Em Programação Orientada a Objetos, costumamos passar dados nos parênteses quando queremos 
que o objeto "nasça" com certas características fixas. No entanto, no nosso código:

A Classe é uma Ferramenta: O NumericProcessor foi desenhado como uma ferramenta genérica. 
Ele não "é" os dados, ele apenas "processa" os dados que lhe enviamos mais tarde.

Flexibilidade: Ao não passarmos a lista no início, podemos usar o mesmo objeto num_proc 
para processar várias listas diferentes, uma a seguir à outra.

Definição do Método: Se olhares para a definição da classe, verás que não escrevemos um 
método def __init__(self, data):. Por isso, o Python usa um construtor padrão que não aceita 
parâmetros. Para que os dados sejam processados, nós passamos a lista num_data apenas quando 
chamamos os métodos específicos, como:
num_proc.validate(num_data) ou num_proc.process(num_data).


O override (ou sobrescrita) acontece sempre que uma subclasse (filha) define um método que 
já existe na sua classe base (mãe). 🧬

No teu código, os overrides estão em todo o lado! Vamos identificá-los:

1. Onde estão os Overrides?
Sempre que vês def process, def validate ou def format_output dentro de NumericProcessor, 
TextProcessor ou LogProcessor, estás a fazer um override dos métodos definidos na classe 
DataProcessor.

Por exemplo, no NumericProcessor:
validate: Estás a substituir o comportamento abstrato pela lógica de somar + 0. 🔢
process: Estás a substituir a promessa original pela lógica de calcular a média. 📈
format_output: Estás a substituir o método base pela tua formatação específica. 📝


No validate() tu fazes algo como:
level = text.split(":", 1)[0].strip().upper()
Isso permite aceitar várias formas de escrever.
Mas o texto original continua:
Error
Se não fizeres upper() no process(), o resultado final pode ficar inconsistente:
Error|Connection timeout

for proc, data in all_data: - proc sao as classes, data é data
        result = proc.process(data) - processamento
        if "|" in result: -- aqui se o result sair com | fazemos o format_output
            formatted = proc.format_output(result)
            print(f"Result {count}: {formatted[8:]}") -- este 8 é para cortar Output ao format
        else:
            print(f"Result {count}: {result}")


SOBRE POLIMORFISMO:

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
Todas as subclasses (NumericProcessor, TextProcessor, LogProcessor) implementam o mesmo método:
process(data)
Então, no loop polimórfico:
all_data = [
    (NumericProcessor(), [1, 2, 3]),
    (TextProcessor(), "Hello World!"),
    (LogProcessor(), "INFO: System ready")
]
for proc, data in all_data:
    result = proc.process(data)
Não importa se é NumericProcessor, TextProcessor ou LogProcessor
O mesmo método process é chamado
Cada classe responde de forma diferente, mas a chamada é uniforme



DUVIDAS NO ex1:

os types sao sempre environmeta no sensor, e sempre finantial data no transaction??

testes para o ex1:

sensor:
ORIGINAL: sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
só com temp
sensor_batch = ["temp:25"]
sem temp
sensor_batch = ["humidity:60", "pressure:1000"]
dois temp
sensor_batch = ["temp:20", "temp:30", "humidity:50"]
estranhos
sensor_batch = []
sensor_batch = ["temp:", "humidity:65"]
sensor_batch = ["temp:", "humidity:"]
sensor_batch = [23, "humidity:"]
[23, "humidity:", "temp:abc", "temp:20", "humidity:abc", "temp"]

transaction
ORGINAL: trans_batch = ["buy:100", "sell:150", "buy:75"]
trans_batch = [23, "buy", "sell:abc", "buy:75"]
trans_batch = []
trans_batch = ["sell:20"]

event
ORIGINAL: event_batch = ["login", "error", "logout"]
event_batch = [45, "error", "logout", "", "log-out"]
event_batch = [45, "log-out", "logout"]
event_batch = [45, "log-out"]



ORIGINAL:
all_batches = [
        ["temp:48", "humidity:80"],
        ["buy:200", "sell:50", "buy:10", "sell:20"],
        ["login", "error", "logout"]
    ]


processor.process_filtered(all_batches, "high")
processor.process_filtered(all_batches)
processor.process_filtered(all_batches, "low")





ex2

JSON (JavaScript Object Notation): * É o formato "rei" da internet hoje em dia. 🌐
Ele organiza os dados em pares de chave: valor, muito parecido com os dict (dicionários) do Python.
Exemplo: {"sensor": "temp", "valor": 23.5}. É fácil de ler tanto para humanos quanto para máquinas.

CSV (Comma-Separated Values): * É o formato clássico das folhas de cálculo (como o Excel). 📊
Os dados são apenas linhas de texto onde cada informação é separada por uma vírgula.
Exemplo: sensor,valor\ntemp,23.5. É muito leve e simples, mas menos flexível que o JSON.

🔌 O que são os Adaptadores (Adapters)?
Na engenharia de software, um Adaptador funciona exatamente como um adaptador de tomada universal. 🔌
O Problema: O seu pipeline principal espera "dados processáveis", mas o JSON chega como uma string complexa 
e o CSV chega como uma linha de texto.
A Solução: Criamos uma classe para cada formato.
O JSONAdapter sabe ler o "idioma" JSON.
O CSVAdapter sabe ler o "idioma" CSV.
O Truque: Ambos herdam da mesma "mãe" (ProcessingPipeline), por isso o sistema pode tratá-los da mesma forma, 
sem se preocupar com o que está lá dentro.

masporque é que o tipo data nao deves er do tipo procesingpipelina?
Essa é uma confusão muito comum e muito importante de esclarecer! 🧠 Vamos separar o "trabalhador" do "material de trabalho".
Imagine uma fábrica de sumos 🍎:
A Máquina (Pipeline): É a estrutura que esmaga, filtra e engarrafa.
A Fruta (Data): É o que entra na máquina para ser transformado.
No teu código:
ProcessingPipeline é a Máquina. Ela tem o método process() (os botões e engrenagens).
data é a Fruta. Pode ser uma string, um int, um dict, ou qualquer outra informação que queiras processar.

⛓️ O Conceito de Pipeline Chaining
Lembras-te da pergunta sobre a "corrente" (chaining)? É aqui que o tipo do data brilha.
Se tivermos 3 pipelines:
Pipeline_A recebe "Maçã" 🍎 e devolve "Sumo" 🧃.
Pipeline_B recebe "Sumo" 🧃 e devolve "Garrafa de Sumo" 🍾.
Pipeline_C recebe "Garrafa de Sumo" 🍾 e devolve "Caixa de Garrafas" 📦.
O data vai mudando de forma, mas as máquinas (pipelines) continuam a ser máquinas.


Ao padronizarmos tudo para um dicionário logo no InputStage, ganhamos três grandes vantagens:
Previsibilidade: As etapas seguintes (Transform e Output) sabem que vão receber sempre um objeto onde 
podem usar o método .get() ou [], independentemente da origem do dado. 🛠️
Expansibilidade: Se amanhã decidires adicionar um formato novo (como XML), só precisas de ensinar o 
InputStage a metê-lo dentro de um dicionário. O resto do pipeline continua a funcionar sem mudares uma única linha de código. 🚀
Metadados: O dicionário permite-nos "colar etiquetas" (novas chaves como "range_status" ou "average") 
ao dado original sem o destruir, mantendo todo o histórico do processamento num só lugar. 🏷️

json.dumps(data): Pega no seu dicionário Python e transforma-o numa string de texto seguindo o 
padrão JSON (que usa sempre aspas duplas "). 📋
Quando fazes print(f"Input: {data}") e o data é uma string, o Python imprime apenas o texto. Mas se o data for uma lista, 
um dicionário ou se usares a biblioteca json, o Python coloca as aspas automaticamente para indicar que aquilo é 
um valor de texto dentro de uma estrutura.

class NexusManager:
    def __init__(self) -> None:
        self.pipelines: list[ProcessingPipeline] = []
        self.record_proc = 0

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def chain_demo(self) -> None:
        print("\n=== Pipeline Chaining Demo ===")
        print("Pipeline A -> Pipeline B -> Pipeline C")
        print("Data flow: Raw -> Processed -> Analyzed -> Stored")
        
        # Aqui usamos o valor acumulado no nosso caderninho! (99 + 1 = 100)
        total = self.record_proc + 1
        
        # 3. Simulação de tempo (0.066 * 3 pipelines (JSON, CSV, STREAM) ≈ 0.2s)
        simulated_time = len(self.pipelines) * 0.066
        
        print(f"Chain result: {total} records processed through "
              f"{len(self.pipelines)}-stage pipeline")
        print(f"Performance: 95% efficiency, {simulated_time:.1f}s total "
              f"processing time")



Em termos simples: o Protocol diz ao Python o que um objeto deve saber fazer, em vez de se preocupar com quem o objeto é.
class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ... # Os três pontos significam que é apenas uma definição
1. O que é o Protocol? 📜
Diferente de uma classe normal ou de uma classe abstrata (ABC), onde tu herdas as características 
(ex: class JSONAdapter(ProcessingPipeline)), o Protocol funciona como uma Interface Estrutural.

Se uma classe tiver um método chamado process que recebe Any e devolve Any, o Python considera que essa classe 
"segue o protocolo", mesmo que tu não tenhas escrito (ProcessingStage) ao lado do nome da classe.

2. Para que serve no teu código? 🛠️
No teu sistema, tu tens vários estágios (InputStage, TransformStage, OutputStage). Todos eles têm uma coisa em comum: o 
método process.

Ao definires o ProcessingStage(Protocol), tu estás a dizer ao sistema:

"Qualquer objeto que tenha um método chamado process pode ser considerado um estágio de processamento."

Isto é muito útil para o Type Checking (verificação de tipos). Se tu tentares adicionar algo à lista self.stages que 
não tenha o método process, o editor de código (como o VS Code ou PyCharm) vai avisar-te imediatamente que aquilo não é 
um "estágio válido".

3. A diferença Visual
Herança (ABC): "Eu sou um filho da Pipeline, por isso herdo os métodos dela." (Relação de família).

Protocolo (Protocol): "Eu não te conheço, mas se tu sabes process, então podes entrar na minha lista." 
(Relação de competência).

No teu caso específico:
Como tu tens:

class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...
Tu poderias mudar a definição da tua lista de estágios na ProcessingPipeline para ser mais rigorosa:

# Em vez de List[Any], usas o Protocolo:
self.stages: List[ProcessingStage] = [] 
Desta forma, o teu código fica blindado! Só entram na lista objetos que saibam processar dados. 🛡️

# O editor de código (ou o mypy) daria um ERRO aqui:
# "Argument 1 to 'add_stage' has incompatible type 'str'; 
#  expected 'ProcessingStage'"
manager.add_stage("Sou apenas um texto") 
Como uma string não tem o método .process(), o Protocolo impede que ela entre no sistema e 
cause um "Crash" mais tarde. 🛡️


testes:
json_pipe.process(None) no error test

temp errada
{"sensor": "temp", "value": "hot", "unit": "C"}

strem errada:
stream_data = {
        "raw": "Real-time sensor stream",
        "readings": [21.0, "bad", 23.0]
    }
