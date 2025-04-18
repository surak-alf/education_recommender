import torch
from torch_geometric.data import Data
from model import CourseRecommender
from utils import load_data

def train():
    # Load data
    data = load_data()
    
    # Initialize model
    model = CourseRecommender(
        num_students=data.num_students,
        num_courses=data.num_courses
    )
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    
    # Training loop
    for epoch in range(200):
        optimizer.zero_grad()
        out = model(data)
        
        # Simple link prediction loss (grades as edge weights)
        loss = torch.nn.functional.mse_loss(
            out[data.edge_index[0]], 
            data.y.view(-1, 1)
        )
        loss.backward()
        optimizer.step()
        
        if epoch % 20 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
    
    # Save model
    torch.save(model.state_dict(), "./gnn_model/model_weights.pth")
    print("Training complete. Model saved to 'gnn_model/model_weights.pth'.")

if __name__ == "__main__":
    train()