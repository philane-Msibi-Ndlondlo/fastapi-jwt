from passlib.context import CryptContext

class PasswordUtils:
    """
    
    Password Hashing Operations
    
    """
    
    def __init__(self) -> None:
        """
        
        Initialize the passlib context
        
        """
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    
    async def hash_password(self, password: str) -> str:
        """
        
        Hashes the password

        Args:
            password (str): decyphered password of the user to be hashed

        Returns:
            str: hashed password
        """
        return self.pwd_context.hash(password)
    
    async def verify_password(self, password: str, hashed_password: str) -> str:
        """
        
        Verify if the password is the hashed password

        Args:
            password (str): decyphered password of the user to be hashed
            hashed_password (str): cyphered password of the user

        Returns:
            _type_: _description_
        """
        return self.pwd_context.hash(password, hashed_password)
    
passwordUtils = PasswordUtils()
        
        