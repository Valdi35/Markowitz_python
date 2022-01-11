class optimMarkowitz:
  """ 
  La classe contient les différentes méthodes d'optimisation du modèle de Markowitz.
  Vous devez avoir installé la librairie numpy sur votre machine.
  """
  def __init__(self,returns,riskMat,w,lbda,methode):
    self.returns = returns
    self.riskMat = riskMat
    self.w = w
    self.lbda = lbda

  def rendementCible(riskMat,w):
    """
    riskMat : Covariance matrix of portfolio assets, must be a N*N matrix
              with N the numbers of assets in portfolio
    x : initially weighted portfolio, must be a N*1 matrix 
    """
    return np.dot(np.dot(w,riskMat),w.T)

  def riskCible(w,riskMat,returns):
    """
    riskMat : Covariance matrix of portfolio assets, must be a N*N matrix
              with N the numbers of assets in portfolio
    x : initially weighted portfolio, must be a N*1 matrix 
    r : vector of means returns, N*1 matrix
    """
    return np.dot(np.dot(w,riskMat),w.T) - np.dot(w,returns)

  def penaLized(w,risk,returns,lbda=0.001):
      """
    riskMat : Covariance matrix of portfolio assets, must be a N*N matrix
              with N the numbers of assets in portfolio
    x : initially weighted portfolio, must be a N*1 matrix 
    r : vector of means returns, N*1 matrix
      lambda : Regularization parameter
      maximization is a minimization of -1*function()
      """
      return - (np.dot(w,returns) - np.dot(np.dot(w,riskMat),w.T) - lbda * (np.dot(np.dot(w,np.eye(len(w))),w.T)))
