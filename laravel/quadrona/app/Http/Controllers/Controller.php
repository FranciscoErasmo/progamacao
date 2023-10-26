<?php

namespace App\Http\Controllers;
use App\Models\Endereco;
use App\Models\Cliente;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Http\Request;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;

class Controller extends BaseController
{
    use AuthorizesRequests, ValidatesRequests;
    public function index(){

        return view('welcome');
    }


public function endereco(){
    $endereco = Endereco::all();
    return view('endereco', compact('endereco'));
    }
    public function cliente(){
        $cliente = cliente::all();
        return view('cliente', compact('cliente'));
        }


public function criar(Request $request){
    $endereco = new Endereco();
    $endereco->cep = $request->input('cep');
    $endereco->rua = $request->input('rua');
    $endereco->bairro = $request->input('bairro');
    $endereco->cidade = $request->input('cidade');
    $endereco->estado = $request->input('uf');
    $endereco->numero = $request->input('numero');
    $endereco->complemento = $request->input('complemento');
    $endereco->save();

    $cliente = new Cliente();
    $cliente->nome = $request->input('nome');
    $cliente->telefone = $request->input('telefone');
    $cliente->email = $request->input('email');
    $cliente->endereco_id = $endereco->id;
    $cliente->save();

    }
}
