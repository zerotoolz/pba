pragma solidity ^0.5.8;
contract PoC_Bioid_Auth {
	mapping (string => address) UserBlockchainAddress ;
    string IBV1CloudLink = "";
    string IBV1CloudHash = "";
    string IBV2LocalHash = "";
	event Create(string Login, string IBV1CloudHash, string IBV1CloudLink, string IBV2LocalHash);
	function createAccount(string memory _Login, string memory _IBV1CloudHash, string memory _IBV1CloudLink, string memory _IBV2LocalHash) public {
		require(bytes(_Login).length <= 32);
		require(bytes(_Login).length > 2);
		IBV1CloudHash = _IBV1CloudHash;
		IBV1CloudLink = _IBV1CloudLink;
	    IBV2LocalHash = _IBV2LocalHash;
		require(UserBlockchainAddress[_Login] == address(0));
		UserBlockchainAddress[_Login] = msg.sender;
		emit Create(_Login, _IBV1CloudHash, _IBV1CloudLink, _IBV2LocalHash);
    }
	function GetIBV1CloudLink(string memory Login) public view returns (string memory){
		return IBV1CloudLink;
	}
	function GetIBV1CloudHash(string memory Login) public view returns (string memory){
		return IBV1CloudHash;
	}
	function GetIBV2LocalHash(string memory Login) public view returns (string memory){
		return IBV2LocalHash;
	}
	function GetUserBlockchainAddress(string memory Login) view public returns (address){
		return UserBlockchainAddress[Login];
	}
}