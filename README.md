# Python: Aplicando a Orientação a Objetos

## Descrição

Este repositório contém o projeto desenvolvido durante o curso **"Python: Aplicando a Orientação a Objetos"** da Alura. O objetivo foi consolidar conhecimentos sobre **POO (Programação Orientada a Objetos)** em Python, criando um sistema simples de gerenciamento de restaurantes.

## O que aprendi

### 1. **Conceitos Básicos de POO**
- **Classes e Objetos**: Como estruturar classes e instanciar objetos.
- **Encapsulamento**: Proteção de atributos com `_` (protegido) e `__` (privado).
- **Métodos de Classe e de Instância**: Diferenças entre `@classmethod` e métodos normais.

### 2. **Especialização com `@property`**
- Uso do **property** para criar atributos calculados e personalizar getters e setters.

### 3. **Métodos Especiais**
- **`__init__`**: Método construtor para inicialização de atributos.
- **`__str__`**: Representação textual dos objetos.

### 4. **Organização do Código**
- Criação de **módulos** (`avaliacao.py` e `restaurante.py`) para separar responsabilidades.
- Importação de classes entre arquivos com `from modelos.restaurante import Restaurante`.

### 5. **Trabalhando com Listas e Objetos**
- Lista de restaurantes armazenada como atributo de classe.
- Lista de avaliações armazenada dentro de cada restaurante.

### 6. **Validações e Regras de Negócio**
- Impedir notas inválidas em avaliações.
- Cálculo da média de avaliações.
- Alternância de estado do restaurante (ativo/inativo).

## Estrutura do Projeto

```
projeto/
│-- modelos/
│   ├── restaurante.py
│   ├── avaliacao.py
│-- app.py
│-- README.md
```

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/delberss/curso-alura-python-aplicando-orientacao-objetos
   ```

2. Entre no diretório:
   ```bash
   cd curso-alura-python-aplicando-orientacao-objetos
   ```

3. Execute o programa:
   ```bash
   python app.py
   ```

## Próximos Passos
- Melhorar a interface de saída no terminal.
- Adicionar persistência de dados (salvar avaliações em um banco de dados ou arquivo JSON).
- Criar testes automatizados para validação das regras de negócio.

---

**Curso:** [Python: Aplicando a Orientação a Objetos - Alura](https://cursos.alura.com.br/course/python-aplicando-orientacao-objetos)

