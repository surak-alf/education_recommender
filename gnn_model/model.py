import torch
from torch_geometric.nn import GATConv

class CourseRecommender(torch.nn.Module):
    def __init__(self, num_students, num_courses, hidden_dim=64):
        super().__init__()
        self.student_embed = torch.nn.Embedding(num_students, hidden_dim)
        self.course_embed = torch.nn.Embedding(num_courses, hidden_dim)
        self.conv1 = GATConv(hidden_dim, hidden_dim)
        self.conv2 = GATConv(hidden_dim, hidden_dim)
        
    def forward(self, data):
        # Embed students and courses
        student_embs = self.student_embed(torch.arange(data.num_students))
        course_embs = self.course_embed(torch.arange(data.num_courses))
        x = torch.cat([student_embs, course_embs], dim=0)
        
        # Graph convolutions
        x = self.conv1(x, data.edge_index)
        x = torch.relu(x)
        x = self.conv2(x, data.edge_index)
        
        return x