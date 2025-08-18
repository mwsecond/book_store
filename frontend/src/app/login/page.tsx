
const TelaLogin = () =>{

    return (
        <div className="max-w-7xl mx-auto mt-6">
      {/* Formulário de login, que chama enviaDados ao submeter */}
      <form className="folha" 
        /*onSubmit={}*/
        >
        
        <h3>Login</h3>

        {/* Campo para email */}
        <div className="mb-5">
          <label htmlFor="email" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">E-mail do Cliente:</label>
          <input 
            type="email" 
            id="email" 
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
            placeholder="name@flowbite.com" 
            required 
            /*{...register("email")}*/ // conecta o input ao react-hook-form
            />
        </div>

        {/* Campo para senha */}
        <div className="mb-5">
          <label htmlFor="password" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Senha de Acesso:</label>
          <input 
            type="password" 
            id="password" 
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
            required 
            /*{...register("senha")}*/ // conecta o input ao react-hook-form
            />
        </div>

        {/* Botão de envio do formulário */}
        <button 
          type="submit" 
          className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
          Entrar
        </button>
      </form>

      {/* Link para página de cadastro caso o usuário não tenha conta */}
      <p className="mt-4 text-center">
          Não possui conta?{' '}
          <a href="/cadastro" className="text-blue-600 hover:underline">
            Cadastre-se
          
          </a>
      </p>

      {/* Componente para exibir mensagens toast no topo direito da tela */}
    </div>
  )
}
export default TelaLogin