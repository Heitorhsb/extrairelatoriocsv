# extrairelatoriocsv
Extrai csv de banco mongodb e envia por email com o csv em anexo



O executa_consulta_quizz.sh é necessário parar osquestrar os outros scripts, o executa_consulta_quizz.sh é o primeiro a ser executado, na minha necessidade ele altera uma tabela no banco antes de executar os scripts,
o coleta.py coleta do banco mongodb e salva em um arquivo chamado collection.txt, o corrigejson.py corrige e transforma o txt em json, o reprocessajson.py corrige errdos da conversão e o enviarelatorio.py envia o arquivo nomes.csv por email.