<!DOCTYPE html>
<html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <title>QUADRONA</title>
</head>
<body>
<table class="table">
  <thead>
    <tr>
      <th scope="col">ID</th>
      <th scope="col">nome</th>
      <th scope="col">email</th>
      <th scope="col">telefone</th>
    </tr>
  </thead>
  <tbody>
    @foreach ($cliente as $cliente)

    <tr>
      <th scope="row">{{$cliente->id}}</th>
      <td>{{$cliente->nome}}</td>
      <td>{{$cliente->email}}</td>
      <td>{{$cliente->telefone}}</td>
    </tr>
    @endforeach

  </tbody>
</table>
</body>
</html>
