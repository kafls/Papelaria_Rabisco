export default function Titulo(props){
    console.log(props)
    return(
        <h1 className='display-5 text-success text-center mt-3'>
            {props.texto}
        </h1>
    )
}