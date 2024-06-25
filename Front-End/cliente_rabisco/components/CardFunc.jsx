export default function CardFunc(props) {
    return (
        <div className="card">
            <div className="col">
                <div className="card">
                <img src={`${props.avatar}`} className="card-img-top" alt="..." />
                <div className="card-body">
                    <h5 className="card-title">{props.first_name} {props.last_name}</h5>
                    <p className="card-text">{props.email}</p>
                </div>
                </div>
            </div>
        </div>
    )
}
CardFunc.defaultProps = {
    first_name: 'Nome',
    last_name: 'Sobrenome',
    email: 'first_name@gmail.com',
    avatar: 'avatar'
}

