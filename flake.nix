{
  description = "QR generator";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = {nixpkgs, ...}:
  let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.x86_64-linux.default = pkgs.mkShell {
      nativeBuildInputs = with pkgs; [
        python313
        python313Packages.qrcode
        python313Packages.pillow
      ];
    };
  };
}
