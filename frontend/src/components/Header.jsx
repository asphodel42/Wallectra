function Header({ loggedIn }) {
  return (
    <>
      <header className="header">
        <div className="header-cont">
          <div className={`header-logo ${loggedIn ? "logged-in" : ""}`}>
            <div className="header-logo-img">
              <img src="./public/Logo/Wallectra-clear-logo.png" alt="" />
            </div>
            <div className="header-logo-text">
              <h1>Wallectra</h1>
            </div>
          </div>
          <div className={`header-btn ${loggedIn ? "logged-in" : ""}`}>
            <button>
              <p>Log out</p>
            </button>
          </div>
        </div>
      </header>
    </>
  );
}

export default Header;
