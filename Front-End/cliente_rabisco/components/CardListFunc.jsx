import CardFunc from "./CardFunc"

export default function CardListFunc(props){
    const {funcionarios} = props
    return(
        <div className="container">
                <div className="row g-3">
                    {funcionarios.map(function (funcionario, index){
                        return(
                            <div className="col-12 col-sm-6 col-md-4 col-lg-3" key={index}>
                                <CardFunc
                                    first_name={funcionario.first_name}
                                    last_name={funcionario.last_name}
                                    email={funcionario.email}
                                    avatar={funcionario.avatar}
                                />
                            </div> 
                        )
                    })}

                </div>
            </div>
    )
}


