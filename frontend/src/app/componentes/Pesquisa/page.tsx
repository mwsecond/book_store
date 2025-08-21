import './Pesquisa.css';

function Pesquisa() {


  return (
    <div className="pesquisa-container">
      <form className="pesquisa-form">
        <div className="pesquisa-org">
          <span className="icon-lupa">
            <svg
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 20 20"
            >
              <path
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
              />
            </svg>
          </span>
          <input
            type="search"
            name="pesq"
            id="default-search"
            placeholder="Informe título"
            required
            className="pesquisa-input"
          />
          <button type="submit" className="botao-pesquisar">
            Pesquisar
          </button>
        </div>
      </form>
    </div>

  );
}

export default Pesquisa;
