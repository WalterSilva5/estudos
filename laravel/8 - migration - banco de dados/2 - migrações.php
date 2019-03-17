uma migração é a execução de um codigo sql

antes de tudo exclui os dois arquivos da pasta:
database/migrations

criar migração:
php artisan make:migration nome_da_migracao

ao executar esse codigo os arquivos com a migração serão 
criados na pasta: database/migrations

ex de migração:
php artisan make:migration criar_tabela_produtos --create=produtos

esse parametro --create=produtos serve para criar um template
de criação de tabela para a migration