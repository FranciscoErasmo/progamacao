<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Controller;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', [Controller::class,'index'])->name('index');
Route::get('endereco', [Controller::class, 'endereco'])->name('endereco');
Route::post('criar/endereco', [Controller::class, 'criar'])->name('criar');
Route::get('cliente', [Controller::class, 'cliente'])->name('cliente');
