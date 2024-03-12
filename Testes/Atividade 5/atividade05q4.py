class SecuritySystem:

    def __init__(self):
        self.password = "1234"
        self.verification_code = "9898"
        self.max_attempts = 3

    def verify_account(self):
        for attempt in range(self.max_attempts):
            user_password = input("Digite sua senha: ")
            user_verification_code = input("Digite seu código de verificação: ")

            if user_password == self.password and user_verification_code == self.verification_code:
                print("Seus dados foram verificados. Bem-vindo!")
                break
            else:
                remaining_attempts = self.max_attempts - (attempt + 1)
                print(f"Tentativa inválida. Você tem {remaining_attempts} tentativas restantes.")

        else:
            print("Sua conta foi bloqueada. Entre em contato com o suporte.")

security_system = SecuritySystem()
security_system.verify_account()