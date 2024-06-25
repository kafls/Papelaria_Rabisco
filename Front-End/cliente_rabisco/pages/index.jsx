import HeaderB from '../components/HeaderB'
import Titulo from '@/components/Titulo'
import Carrosel from '@/components/Carrosel'

export default function home(){ 
    return(
        <>
        <HeaderB title="Home"/>
        <Titulo texto="Bem-vindo à Papelaria Rabisco!"/>
        <Carrosel />
        </>
    )
}
